# -*- coding: utf-8 -*-
"""Views module for posts app."""
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.settings import THEME
from lib.util import get_http_referer
from common.contexts import get_common_view_context
from analytics.models import PageRequest
from .models import Category, Post


def post_detail(request, slugged_title):
    """View for /post/{}"""
    try:
        post = Post.objects.get(slugged_title=slugged_title, is_published=True)
    except Post.DoesNotExist:
        return HttpResponseRedirect('/')

    page_request = PageRequest.objects.create(
        name='Post - {}'.format(slugged_title),
        url='/post/{}'.format(slugged_title),
        ip_addr=request.META['REMOTE_ADDR'],
    )

    http_referer = get_http_referer(request)

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    view_context = {
        'page_title': post.title,
        'post': post,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/posts_post.html'.format(THEME),
        view_context,
    )


def posts_filtered(request):
    """View for /posts/filter/?category_name={}"""
    http_referer = get_http_referer(request)

    page_request = PageRequest.objects.create(
        name='Filtered Post - {}'.format(request.GET['category_name']),
        url='/posts/filtered/{}'.format(request.GET['category_name']),
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    filt = request.GET['category_name']

    category = Category.objects.get(name=filt)

    post_list = Post.objects.filter(
        categories__in=[category],
        is_published=True,
    ).order_by('-created')

    view_context = {
        'page_title': 'Post by Category: {}'.format(category.name),
        'post_list': post_list,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/common_index.html'.format(THEME),
        view_context,
    )
