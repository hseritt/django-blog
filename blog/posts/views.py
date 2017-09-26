# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, Post

def post_detail(request, post_id):

    post = Post.objects.get(pk=post_id)
    category_list = Category.objects.filter(display=True)

    return render(
        request,
        'posts_post.html',
        {
        	'category_list': category_list,
        	'page_title': 'Post: {}'.format(post.title),
            'post': post,
        }
    )

