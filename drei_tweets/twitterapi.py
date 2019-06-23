# -*- coding: utf-8 -*-
"""
Sjoerd Gnodde

Saves all the tweets to a JSON file. Has commented out section to plot and save to file.
"""

# Import everything

#import matplotlib.pyplot as plt
#import pandas as pd
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
sys.path.insert(0, 'C:/Users/Sjoerd Gn/Documents/git/passwords')

import twitter_api_credentials as twit_cred

#from mpl_toolkits.basemap import Basemap
#import json


# Live Plot 
"""
fig = plt.figure(figsize=(15, 15))
m = Basemap(resolution=None, lat_0=0, lon_0=-0)
m.bluemarble(scale=1);
"""

class TwitterStreamer():
    
    """
    Streaming and processing live tweets
    """
    def __init__(self):
        pass
    
    def stream_tweets(self, save_tweets_filename, substring_check):
        
        # Twitter authentication and the connection 
        # to the Twitter API
        
        listener = StdOutListener(save_tweets_filename)
        auth = OAuthHandler(twit_cred.CONSUMER_KEY, 
                            twit_cred.CONSUMER_SECRET)
        auth.set_access_token(twit_cred.ACCESS_TOKEN, 
                              twit_cred.ACCESS_TOKEN_SECRET)
    
        stream = Stream(auth, listener)
        stream.filter(track=substring_check)

class StdOutListener(StreamListener):
    
    """
    Basic listener. Prints received tweets to standard out.
    """
    
    def __init__(self, save_tweets_filename):
        self.save_tweets_filename = save_tweets_filename
    
    
    def on_data(self, data):
        try:
            
            # Live plot
            """
            json_data = json.loads(data)
            print(json_data['text'])
            all_coor = json_data['coordinates']
            if all_coor:    
                exact_coor = all_coor['coordinates']
                m.scatter(exact_coor[0],exact_coor[1],3,marker='o',color='y')
                print("||||||||||||||||||||||New location!")
                plt.show()
            """
                
            
            # Write to file
            with open(self.save_tweets_filename, "a", newline = '') as tf:
                tf.write(data)
            
            return True
        
        except BaseException as e:
            print("Error on_data: {e}".format(e=e))
        return True
    
    def on_error(self, status):
        print(status)
    

if __name__ == "__main__":
    
    # What do I track?
    substring_check = ['pils', 'zuipen', 'beer', 'drinks', 'drei', 'dopie']
    
    # Where do I save it to
    save_tweets_filename = "output/tweets.json"
    
    # Load streamer
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(save_tweets_filename, substring_check)
    

    
"""
password_loc = "../passwords/twitter.csv"

unpw = pd.read_csv(password_loc)


username = unpw['username'][0]
password = unpw['password'][0]
"""