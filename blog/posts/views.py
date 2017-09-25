# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

def post_detail(request, post_id):

    post = Post.objects.get(pk=post_id)

    return render(
        request,
        'posts_post.html',
        {
            'post': post,
        }
    )

