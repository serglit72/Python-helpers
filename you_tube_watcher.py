#you_tube_watcher.py
import json
import urllib3
import sys
from selenium import webdriver
import time


def look_test_video():
    api_key = 'AIzaSyD2w1SP-naf0i7QMD1sbUodi9nMZvx_Fag'
    channel_id = "UCmLtfbz4VuosR0J0uU0bt3A" #Alarm Timer

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    url = (base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key,channel_id))
    http = urllib3.PoolManager()
    inp = (http.request('GET',url)).data


    resp = json.load(inp)
    print(resp)
    vidID = resp['items'][0]['id']['videoId']
    
    video_exists = False
    with open('videoid.json', 'a') as json_file:
      data = json.loads(json_file)
      if data['videoId'] != vidID:
          driver = webdriver.Firefox()
          driver.get(base_video_url+vidID)
          video_exists = True
    if video_exists:
        with open('videoid.json','w') as json_file:
            data = {'videoId' : vidID}
            json.dump(data,json_file)
look_test_video() 
