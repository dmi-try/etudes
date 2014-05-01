#!/usr/bin/env ruby

require './etude3.rb'

describe 'helpers' do
  it 'valid_number? should accept only one digit numbers' do
    valid_number?(4).should eq(true)
    valid_number?(1).should eq(true)
    valid_number?(9).should eq(true)
    valid_number?(0).should eq(false)
    valid_number?(10).should eq(false)
    valid_number?(4.0).should eq(false)
    valid_number?(nil).should eq(false)
    valid_number?([]).should eq(false)
    valid_number?([1]).should eq(false)
  end
  it 'valid_coords? should accept array of two integer numbers' do
    valid_coords?([]).should eq(false)
    valid_coords?([1, 1]).should eq(true)
    valid_coords?([1.0, 1.0]).should eq(true)
    valid_coords?([1, 1, 1]).should eq(false)
    valid_coords?([1]).should eq(false)
    valid_coords?([1.5, 1]).should eq(false)
    valid_coords?([0, 0]).should eq(true)
    valid_coords?([2, 2]).should eq(true)
    valid_coords?([3, 2]).should eq(false)
    valid_coords?([-1, 1]).should eq(false)
    valid_coords?(5).should eq(false)
  end
  it 'coords_by_number should return coords of a number' do
    coords_by_number(5).should eq([1, 1])
    coords_by_number(1).should eq([0, 0])
    coords_by_number(10).should eq(nil)
    coords_by_number(1.0).should eq(nil)
  end
  it 'number_by_coords should return number' do
    number_by_coords([1, 1]).should eq(5)
    number_by_coords(nil).should eq(nil)
    number_by_coords([2, 2]).should eq(9)
    number_by_coords([1.5, 1]).should eq(nil)
  end
  it 'number_in_between should return valid number or nil' do
    number_in_between(1, 3).should eq(2)
    number_in_between(1, 7).should eq(4)
    number_in_between(3, 7).should eq(5)
    number_in_between(7, 9).should eq(8)
    number_in_between(1, 6).should eq(nil)
  end
  it 'key_length should return length' do
    key_length([1, 2]).should eq(1)
    key_length([1, 2, 5, 7]).should be_within(0.5).of(3.5)
    key_length([]).should eq(0)
    key_length([1]).should eq(0)
  end
  it 'valid_key? should check key' do
    valid_key?(1).should eq(false)
    valid_key?([1]).should eq(true)
    valid_key?([]).should eq(false)
    valid_key?([1, 2]).should eq(true)
    valid_key?([1, 2, 3, 4, 5, 6, 7, 8, 9]).should eq(true)
    valid_key?([1, 3]).should eq(false)
  end
  it 'iterate_keys should work' do
    expect {|b| iterate_keys([1, 2], &b)}.to yield_successive_args([1, 2], [1], [2, 1], [2], [])
    expect {|b| iterate_keys([], &b)}.to yield_successive_args([])
  end
end
