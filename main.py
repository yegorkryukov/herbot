
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
from config import *


# In[2]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
# Weather API Key
api_key = weather_api_key


# In[5]:


def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Moscow"
    units = "metric"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

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


# In[6]:


# Infinite loop
while True:
    WeatherTweet()
    time.sleep(3600)

