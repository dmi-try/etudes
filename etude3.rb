#!/usr/bin/env ruby

# Find a longest path for 9 points keychain
# Key format: numbers in a row: 123456789 or 154 or 391 etc
# Iterator
# Filter incorrect keys
# Calculate length of the key

def iterate_keys(extra_numbers)
  extra_numbers.each do |x|
    iterate_keys(extra_numbers - [x]) {|y| yield [x]+y}
  end
  yield []
end

def valid_number?(num)
  num.is_a?(Integer) && num.between?(1,9)
end

def valid_coords?(coords)
  if coords.is_a?(Array) && coords.size == 2
    (coords[0] % 1 == 0) && coords[0].between?(0,2) && (coords[1] % 1 == 0) && coords[1].between?(0,2) 
  else
    false
  end
end

def coords_by_number(num)
  if valid_number?(num)
    [(num-1) % 3, (num-1) / 3]
  end
end

def number_by_coords(coords)
  if valid_coords?(coords)
    ((coords[0] + 1) + (coords[1] * 3)).to_int
  end
end

def number_in_between(a, b)
  if valid_number?(a) && valid_number?(b)
    coords = [coords_by_number(a), coords_by_number(b)].transpose.map{|x| x.reduce(:+)/2.0}
    number_by_coords(coords)
  end
end

def key_length(key)
  if key.size < 2
    return 0
  end
  if key.size > 2
    return key_length(key[0,2]) + key_length(key[1, key.size-1])
  end
  coords_a = coords_by_number(key[0])
  coords_b = coords_by_number(key[1])
  return ((coords_a[0]-coords_b[0])**2 + (coords_a[1]-coords_b[1])**2)**0.5
end

def valid_key?(key)
  if !key.is_a?(Array) || key.size == 0
    return false
  end
  0.upto(key.size - 2) do |i|
    middle = number_in_between(key[i], key[i+1])
    if valid_number?(middle)
      unless (key[0, i].include?(middle) rescue false)
        return false
      end
    end
  end
  true
end

if __FILE__ == $0
  max_l = 0
  keys = []
  iterate_keys([1,2,3,4,5,6,7,8,9]) do |key|
    if valid_key?(key)
      key_l = key_length(key)
      if key_l == max_l
        keys += [key]
      end
      if key_l > max_l
        max_l = key_l
        keys = [key]
      end
      printf "key: %-27s   length: %6.2f   max: %6.2f\n", key, key_l, max_l
    end
  end
  print "Winners:\n"
  keys.each { |key| print "#{key}\n" }
end
