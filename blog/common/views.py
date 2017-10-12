# -*- coding: utf-8 -*-
"""Views module for common app."""
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Post
from common.contexts import get_common_view_context
from analytics.models import PageRequest


def index(request):
    """View for /"""
    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = None

    page_request = PageRequest.objects.create(
        name='Index',
        url='/',
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    post_list = Post.objects.all().order_by('-published')

    view_context = {
        'page_title': 'Welcome to {}'.format(SITE_NAME),
        'post_list': post_list,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        'common_index.html',
        view_context,
    )


def about(request):
    """View for /about/"""
    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = ''

    page_request = PageRequest.objects.create(
        name='About',
        url='/about',
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    view_context = {
        'page_title': 'About',
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        'common_about.html',
        view_context,
    )
