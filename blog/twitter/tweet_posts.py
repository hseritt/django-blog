#!/usr/bin/env python


import django
import os
import sys

from random import choice

sys.path.append('.')
sys.path.append('..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

django.setup()

# pylint: disable=E402
from posts.models import Post

if __name__ == '__main__':
    post_list = Post.objects.filter(is_published=True)
    post = choice(post_list)
    print(post)
