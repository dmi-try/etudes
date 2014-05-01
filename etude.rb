#!/usr/bin/env ruby

# Задачка про программиста и кофе
# Программист пишет одну строку за 1 минуту. Каждую следующую - в tired_factor раз дольше.
# В любой момент он может выпить кофе, что сбросит счетчик обратно. Но питье кофе
# отнимает coffee_time времени. Всего кофе можно выпить break_count раз.
# Рассчитать минимальное время, необходимое для написания lines_count строк,
# а также максимальное количество строк за work_time минут.

@tired_factor = 2
@coffee_time = 10
@lines_count = 50
@break_counts = @lines_count - 1
@work_time = 49

def calc_lines_schedule(breaks)
  line_time = 1
  schedule = []
  1.upto(@lines_count) do |line_num|
    schedule += [line_time]
    line_time *= @tired_factor
    if [line_num] & breaks != []
      line_time = 1; schedule += [@coffee_time]
    end
  end
  schedule
end

def sum(array)
  sum = 0
  array.each {|i| sum+=i}
  sum
end

old_time=nil
1.upto(@break_counts) { |iter_breaks|
  breaks = []
  1.upto(iter_breaks) { |i| breaks += [@lines_count*i/(iter_breaks+1)] }
  schedule = calc_lines_schedule(breaks)
  time = sum(schedule)
  break if old_time and time > old_time
  old_time = time
  puts iter_breaks.to_s + ": " + breaks.join(",") + " => " + schedule.join(",") + "=" + time.to_s
}
