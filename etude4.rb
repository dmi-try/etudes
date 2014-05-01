#!/usr/bin/env ruby

# Download all the stickers from vk.com/images/stickers/(\d+)/(?size).png
# Input: size in pixels (64,128,256,any other?)

require 'open-uri'

max_id = 168
sizes = [64, 128, 256]

def calc_url(id, size)
  "https://vk.com/images/stickers/#{id}/#{size}.png"
end

def calc_filename(id, size)
  "size_%03d/sticker_%03d_%03d.png" % [size, id, size]
end

if __FILE__ == $0
  Dir.mkdir("etude4_stickers") unless File.exists?("etude4_stickers")
  sizes.each do |size|
    Dir.mkdir("etude4_stickers/size_%03d" % size) unless File.exists?("etude4_stickers/size_%03d" % size)
  end
  Dir.chdir "etude4_stickers"
  1.upto(max_id) do |id|
    print "ID #{id}:"
    sizes.each do |size|
      print " #{size}"
      open(calc_filename(id, size), 'wb') do |file|
        file << open(calc_url(id, size)).read
      end
    end
    print "\n"
  end
end
