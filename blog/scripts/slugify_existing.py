#!/usr/bin/env python

import os
import sys

sys.path.append('.')
sys.path.append('..')

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

import django
from django.utils.text import slugify


django.setup()

from posts.models import Post


if __name__ == '__main__':
    post_list = Post.objects.filter(slugged_title=None)

    for post in post_list:
        print(post.title)
        print(slugify(post.title))
        post.slugged_title = slugify(post.title)
        post.save()
        print('\n')

