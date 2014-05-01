require "./bulls_and_cows.rb"
require 'rspec'

describe BullsAndCows do
  before(:each) do
    @game = BullsAndCows.new
  end

  it 'starts with empty history and unsolved' do
    @game.history.tries.should eq 0
    @game.solved?.should eq false
  end

  it 'finishs the game with four bulls' do
    guess = @game.guess(@game.secret)
    guess['bulls'].should eq 4
    guess['cows'].should eq 0
    @game.solved?.should eq true
  end

  it 'swap two fields returns 2b/2c' do
    secret = @game.secret
    secret[0], secret[1] = secret[1], secret[0]
    guess = @game.guess(secret)
    guess['bulls'].should eq 2
    guess['cows'].should eq 2
    @game.solved?.should eq false
    @game.history.tries.should eq 1
  end

  it 'accepts array as a guess' do
    guess = @game.guess([1, 2, 3, 4])
    guess['bulls'].should be >= 0
    guess['bulls'].should be <= 4
    guess['cows'].should be >= 0
    guess['cows'].should be <= 4
  end

  it 'accepts string as a guess' do
    guess = @game.guess(@game.secret.join)
    guess['cows'].should == 0
    guess['bulls'].should == 4
  end

  it 'can validate input' do
    [ 5, 12354, "hi", [1, 3], [1, 2, 3, 1] ].each do |bad|
      @game.guess_valid?(bad).should be false
    end
    [ 1234, 567, "3456", [5, 4, 3, 2] ].each do |good|
      @game.guess_valid?(good).should be true
    end
  end

  #it 'game vars should present'
  #it 'game methods should present'
  #it 'game methods should work on good data'
  #it 'game methods should fail on bad data'
  #it 'history vars should present'
  #it 'history methods should present'
  #it 'history methods should work on good data'
  #it 'history methods should fail on bad data'
  #it 'hints vars should present'
  #it 'hints methods should present'
  #it 'hints methods should work on good data'
  #it 'hints methods should fail on bad data'
end
