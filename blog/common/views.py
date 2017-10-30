# -*- coding: utf-8 -*-
"""Views module for common app."""
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME, THEME
from lib.util import get_http_referer
from posts.models import Post
from common.contexts import get_common_view_context
from analytics.models import PageRequest


def index(request):
    """View for /"""
    http_referer = get_http_referer(request)

    page_request = PageRequest.objects.create(
        name='Index',
        url='/',
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    post_list = Post.objects.filter(is_published=True).order_by('-published')

    view_context = {
        'page_title': 'Welcome to {}'.format(SITE_NAME),
        'post_list': post_list,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/common_index.html'.format(THEME),
        view_context,
    )


def about(request):
    """View for /about/"""
    http_referer = get_http_referer(request)

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
        '{}/common_about.html'.format(THEME),
        view_context,
    )
