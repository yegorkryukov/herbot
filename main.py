
# coding: utf-8
import os
#from boto.s3.connection import S3Connection
#s3 = S3Connection(os.environ['consumer_key'], \
#                  os.environ['consumer_secret'], \
#                  os.environ['access_token'], \
#                  os.environ['access_token_secret'], \
#                  os.environ['weather_api_key'])


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

#commenting this out because heroku vars should pick up
#from config import *

# Twitter API Keys
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')
# Weather API Key
weather_api_key = os.environ.get('weather_api_key')
#print(weather_api_key)

def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Moscow"
    units = "metric"
    query_url = str(url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units)

    # Perform the API call to get the weather
    r = req.get(query_url)
    print(f'   requested URL: {r.url}')
    
    if r.status_code == 200:
        response = r.json()
        temp = response['main']['temp']
    # Twitter credentials
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
        try:
            api.update_status(f'The weather in {city} is {temp}°C now')
            print('Just tweeted')
        except tweepy.TweepError as e:
            print(e)
            pass      


# Infinite loop
while True:
    WeatherTweet()
    time.sleep(18000)

