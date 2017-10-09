# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from .models import Category, Post
from common.contexts import common_view_context
from analytics.models import PageRequest


def post_detail(request, slugged_title):

    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = ''

    pr = PageRequest.objects.create(
        name='Post - {}'.format(slugged_title),
        url='/post/{}'.fomrat(slugged_title),
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        pr.referer = http_referer
        pr.save()

    post = Post.objects.get(slugged_title=slugged_title)
    
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

    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = ''

    pr = PageRequest.objects.create(
        name='Filtered Post - {}'.format(request.GET['category_name']),
        url='/posts/filtered/{}'.format(request.GET['category_name']),
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        pr.referer = http_referer
        pr.save()

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
