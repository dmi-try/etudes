#!/usr/bin/env ruby

require './etude4'

describe 'helpers' do
  it 'calc_url should show urls' do
    calc_url(168, 64).should eq("https://vk.com/images/stickers/168/64.png")
  end
  it 'calc_filename should return filename' do
    calc_filename(1,128).should eq ("size_128/sticker_001_128.png")
    calc_filename(168,64).should eq ("size_064/sticker_168_064.png")
  end
end
