#!/usr/bin/env python


import django
import os
import sys
import time
import tweepy

from random import choice

sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

django.setup()

# pylint: disable=E402
from blog import env
from twitter.models import Tweet

if __name__ == '__main__':
    while True:
        tweet_list = Tweet.objects.filter(is_active=True)

        auth = tweepy.OAuthHandler(
            env.TW_CONSUMER_KEY,
            env.TW_CONSUMER_SECRET
        )
        auth.set_access_token(env.TW_ACCESS_TOK, env.TW_TOK_SECRET)
        api = tweepy.API(auth)

        for tweet in tweet_list:
            api.update_status(tweet.message)
            time.sleep(86400)
