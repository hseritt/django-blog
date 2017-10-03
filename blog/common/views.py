# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Category, Post
from common.contexts import common_view_context


def index(request):

    post_list = Post.objects.all().order_by('-published')
    
    view_context = {
        'page_title': SITE_NAME,
        'post_list': post_list,
    }

    view_context.update(common_view_context)

    return render(
        request,
        'common_index.html',
        view_context,
    )


def about(request):
    
    view_context = {
        'page_title': 'About',
    }

    view_context.update(common_view_context)

    return render(
        request,
        'common_about.html',
        view_context,
    )
