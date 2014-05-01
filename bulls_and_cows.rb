#!/usr/bin/ruby

require 'logger'
require 'readline'

$log = Logger.new(STDOUT)
$log.level = Logger::WARN

class History
  def initialize
    @steps = []
  end
  def tries
    @steps.length
  end
  def format_line(n, step)
    "#{n}) #{step['guess']} => #{step['bulls']}b/#{step['cows']}c"
  end
  def show
    @steps.each_with_index.map{ |step, i|
      self.format_line(i + 1, step)
    }.join("\n")
  end
  def last
    self.format_line(@steps.length, @steps.last)
  end
  def log(guess, bulls, cows)
    logline = {'guess' => guess, 'bulls' => bulls, 'cows' => cows}
    @steps << logline
    return logline
  end
end

class BullsAndCows
  def initialize
    digits = Array(0..9)
    @secret = 4.times.map{digits.delete_at(rand(digits.size))}
    @history = History.new
    @solved = false
  end
  def secret
    @secret.clone
  end
  def solved?
    @solved
  end
  def history
    @history
  end
  def guess_valid?(guess)
    if guess.class == Fixnum
      guess = "%04d" % guess
    end
    if guess.class == String
      return false if guess !~ /^\d{4}$/
      guess = guess.split('').map(&:to_i)
    end
    return false if guess.size != 4
    guess.each do |i|
      return false if i.class != Fixnum
      return false if i < 0 or i > 9
    end
    10.times do |i|
      return false if guess.count(i) > 1
    end
    true
  end
  def guess(guess)
    guess = "%04d" % guess if guess.class == Fixnum
    guess = guess.split('').map(&:to_i) if guess.class == String
    bulls = cows = 0
    4.times do |i|
      if @secret[i] == guess[i]
        bulls += 1
      else
        cows +=1 if @secret.count(guess[i]) == 1
      end
      $log.debug("D: #{guess[i]}/#{@secret[i]}/#{@secret.count(guess[i])}/#{bulls}b/#{cows}c")
    end
    @solved = true if bulls == 4
    return @history.log(guess, bulls, cows)
  end
end

class Hints
  def initialize
    self.cmd_drop
  end
  def cmd_help
    'Enter number or /[0-9]{4}=[bc-?]{4}'
  end
  def cmd_drop
    @hints = (0..3).map{Array(0..9)}
    'Hints dropped'
  end
  def cmd_show
    4.times.map{ |i| @hints[i].join(' ') }
  end
  def cmd_update(guess, status)
    d = guess
    h = status
    4.times do |i|
      case h[i]
      when 'b'
        4.times do |j|
          @hints[j][d[i]] = 'c' unless i == j
        end
        10.times do |j|
          @hints[i][j] = '-' unless j == d[i]
        end
      when 'c'
        @hints[i][d[i]] = 'c'
      when '-'
        4.times do |j|
          @hints[j][d[i]] = '-'
        end
      end
    end
    self.cmd_show
  end
  def cmd_calc(guess, bulls, cows)
    if bulls == 0
      4.times do |i|
        @hints[i][guess[i]] = '-'
      end
    end
    if cows == 0
      4.times do |i|
        4.times do |j|
          @hints[i][guess[j]] = '-' unless i == j
        end
      end
    end
    if bulls + cows == 4
      4.times do |i|
        10.times do |j|
          @hints[i][j] = '-' unless guess.count(j) == 1
        end
      end
    end
  end
end

def main
  game = BullsAndCows.new
  hints = Hints.new
  puts "I have a secret code of four different digits, try to guess (/? for help)"
  show_hints = false
  abort_game = false
  commands = {
    'help' => {
      'hint' => 'this help screen',
      'cmd' => lambda {
        [<<-'EOHELP'] +

Bulls and Cows game

Your goal is to guess my 4-digits number.  Make your move with your number,
all digits in the number must differ.
Bull means that you have the same digit as me at the same place.
Cow means that you have the same digit as me but on another place.

Any game can be solved in seven turns.

Additional commands:
        EOHELP
        commands.sort.map {|key,value|
          "  /%s - %s" % [key, value['hint']]
        }
      },
    },
    'debug' => {
      'hint' => 'turn on debug messages',
      'cmd' => lambda {
        $log.level = Logger::DEBUG
        'Debug mode on'
      }
    },
    'nodebug' => {
      'hint' => 'turn off debug messages',
      'cmd' => lambda {
        $log.level = Logger::WARN
        'Debug mode off'
      }
    },
    'quit' => {
      'hint' => 'exit the game',
      'cmd' => lambda {
        abort_game = true
        'Good bye'
      }
    },
    'autohints' => {
      'hint' => 'show hints automatically',
      'cmd' => lambda {
        show_hints = true
        'Autohints mode on'
      }
    },
    'autohints' => {
      'hint' => 'do not show hints automatically',
      'cmd' => lambda {
        show_hints = false
        'Autohints mode off'
      }
    },
    'history' => {
      'hint' => 'show completed moves',
      'cmd' => lambda { game.history.show }
    },
    'drop' => {
      'hint' => 'reset hints table',
      'cmd' => lambda { hints.cmd_drop }
    },
    'hints' => {
      'hint' => 'show hints table',
      'cmd' => lambda { hints.cmd_show }
    },
  }
  until game.solved? || abort_game do
    input = Readline.readline("=> ", true)
    input.chomp! if input
    case input
    when nil
      puts commands['quit']['cmd'].call
    when '/?'
      puts commands['help']['cmd'].call
    when /^\/[0-9]{4}=[bc\-\?]{4}$/
      d = input.split('')[1,4].map(&:to_i)
      h = input.split('')[6,4]
      puts hints.cmd_update(d, h)
    else
      if commands.has_key?(input[1..-1])
        puts commands[input[1..-1]]['cmd'].call
      elsif game.guess_valid?(input)
        result = game.guess(input)
        hints.cmd_calc(result['guess'], result['bulls'], result['cows'])
        puts game.history.last
        puts hints.cmd_show if show_hints
      else
        puts 'Please provide 4 different digits or /? for help' if input
      end
    end
  end
  puts game.history.show
  puts "Secret: #{game.secret}, tries: #{game.history.tries}"
end

main if __FILE__ == $0
