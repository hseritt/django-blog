#!/usr/bin/env python
"""Script to slugify existing posts. No longer needed.
"""
import os
import sys
import django
from django.utils.text import slugify
from posts.models import Post


sys.path.append('.')
sys.path.append('..')

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
django.setup()


if __name__ == '__main__':
    POST_LIST = Post.objects.filter(slugged_title=None)

    for post in POST_LIST:
        print post.title
        print slugify(post.title)
        post.slugged_title = slugify(post.title)
        post.save()
        print '\n'
