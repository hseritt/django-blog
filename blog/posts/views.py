# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from .models import Category, Post
from common.contexts import common_view_context


def post_detail(request, post_id):

    post = Post.objects.get(pk=post_id)
    
    view_context = {
        'page_title': post.title,
        'post': post,
    }

    view_context.update(common_view_context)

    return render(
        request,
        'posts_post.html',
        view_context,
    )


def posts_filtered(request):

    filt = request.GET['category_name']

    category = Category.objects.get(name=filt)

    post_list = Post.objects.filter(
        categories__in=[category,]
    ).order_by('-created')

    view_context = {
        'page_title': 'Post by Category: {}'.format(category.name),
        'post_list': post_list,
    }

    view_context.update(common_view_context)

    return render(
        request,
        'common_index.html',
        view_context,
    )
