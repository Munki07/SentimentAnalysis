import tweepy
import pandas as pd

consumer_key = "f6D4c1zDljJNtfkNHfmZhWYct"
consumer_secret = "En4E9LI0Iv8SktdNcnCiRyq0LhS72hZRM4eouGAqZzFxwSS7gn"

access_token = "917067322082213888-cpbY2VeaDMq02nccahoCxV9iye8AXF8"
access_token_secret = "bjMwjFH9WLLBWSkecXGHG6VK7kYi05xNwHvrVADChBvI4"

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret