import os
import tweepy as tw
import pandas as pd

consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

twts= tw.Cursor(api.search,q="Khan Academy",lang="en",since="2020-11-01").items(5)

#list of specific strings we want to check for in Tweets
t = ['KhanAcademy',
    'khan academy',
    'khan Academy!!!',
    'Khan academy!!!',
    'Khanacademy!',
    'Khan Academy!]

for s in twts:
    for i in t:
        if i in s.text:
            sn = s.user.screen_name
            m = "@%s Hello from TalktoVideos!"%(sn)
            s = api.update_status(m,
s.id)
