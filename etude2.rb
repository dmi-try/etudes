#!/usr/bin/env ruby

# Проверка закона Бенфорда на случайных числах. По этому закону в реальных
# данных первая цифра с большей вероятностью окажется единицей (1/3)
# и с куда меньшей - девяткой

# Вывод: закон не работает на случайных числах с фиксированным потолком

numbers = 1000000
max_number = 1000000

def first_digit(n)
  n.to_s[0].to_i
end

counts = Array.new(10, 0)

numbers.times do
  counts[first_digit(rand(max_number))] += 1
end

puts counts
