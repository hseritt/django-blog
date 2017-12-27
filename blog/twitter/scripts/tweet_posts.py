#!/usr/bin/env python


import django
import os
import sys
import time
import tweepy

from random import choice, seed

sys.path.append('.')
sys.path.append('..')
sys.path.append('../..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

django.setup()

# pylint: disable=E402
from blog import env
from posts.models import Post

if __name__ == '__main__':
    seed(time.time())
    post_list = Post.objects.filter(is_published=True, tweet_enabled=True)
    post = choice(post_list)
    title = post.title
    link = post.slugged_title
    msg = '{} - http://dev.prodigi.us/post/{}'.format(title, link)
    auth = tweepy.OAuthHandler(env.TW_CONSUMER_KEY, env.TW_CONSUMER_SECRET)
    auth.set_access_token(env.TW_ACCESS_TOK, env.TW_TOK_SECRET)

    api = tweepy.API(auth)
    api.update_status(msg)
