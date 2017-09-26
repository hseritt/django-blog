# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from posts.models import Category, Post


def index(request):

    post_list = Post.objects.all().order_by('-published')
    category_list = Category.objects.filter(display=True)

    return render(
        request,
        'common_index.html',
        {
            'category_list': category_list,
            'page_title': 'dev.prodidi.us',
            'post_list': post_list,
        },
    )


def about(request):

    return render(
        request,
        'common_about.html',
        {
            'page_title': 'About Harlin',
        }
    )
