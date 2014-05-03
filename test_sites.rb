#!/usr/bin/env rspec

# Make sure that all my sites are accessible

require 'net/http'
require 'open-uri'

describe 'helpers' do
  it 'pyzhov.ru should work' do
    open('http://www.pyzhov.ru/').read.should include 'Пыжов'
    open('http://www.pyzhov.ru/').read.should_not include 'Пыжв'
    lambda{open('http://www.pyzhov.ru/.htaccess')}.should raise_error(OpenURI::HTTPError, "403 Forbidden")
    open('http://www.pyzhov.ru/wp-content/themes/twentyeleven/style.css').read.should include 'Eleven'
    open('http://www.pyzhov.ru/2012/05/10/hello-world/').read.should include 'Привет, мир!'
  end

  it 'pyzhov.ru/2048 should work' do
    open('http://www.pyzhov.ru/2048/js/application.js').read.should include 'render the game'
    open('http://www.pyzhov.ru/2048/').read
  end

  it 'pyzhov.ru redirects should work' do
    Net::HTTP.get_response(URI.parse('http://pyzhov.ru/'))['location'].should eq 'http://www.pyzhov.ru/'
    Net::HTTP.get_response(URI.parse('http://pyzhov.ru/bla-bla'))['location'].should eq 'http://www.pyzhov.ru/bla-bla'
    Net::HTTP.get_response(URI.parse('http://dima5.ru/'))['location'].should eq 'http://www.pyzhov.ru/'
    Net::HTTP.get_response(URI.parse('http://dima5.ru/bla-bla'))['location'].should eq 'http://www.pyzhov.ru/bla-bla'
  end

  it 'rabid-rabbit.ru should work' do
    Net::HTTP.get_response(URI.parse('http://www.rabid-rabbit.ru/'))['location'].should eq 'http://rabid-rabbit.ru/'
    Net::HTTP.get_response(URI.parse('http://www.rabid-rabbit.ru/bla-bla'))['location'].should eq 'http://rabid-rabbit.ru/bla-bla'
    open('http://rabid-rabbit.ru/').read.should include 'Rabid Rabbit'
    open('http://rabid-rabbit.ru/back.png')
  end

  it 'flockman.ru should work' do
    open('http://www.flockman.ru/').read.should include 'sales@flockman.ru'
    open('http://flockman.ru/').read.should include 'sales@flockman.ru'
    open('http://www.flockman.ru/node/17').read.should include '1 марта 2012'
  end
end
