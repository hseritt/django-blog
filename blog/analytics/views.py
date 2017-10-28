# -*- coding: utf-8 -*-
"""Views module for analytics app.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from blog.settings import SITE_NAME, THEME
from common.contexts import get_common_view_context
from posts.models import Post
from .models import PageRequest


def user_is_admin(user):
    """Returns True if user is a superuser. Essentially a check for admin."""
    return user.is_superuser


@user_passes_test(user_is_admin, login_url='/admin/login/')
def index(request):
    """View for /analytics/"""
    post_list = Post.objects.all().order_by('-created')

    for p in post_list:
        p.hits = len(
            PageRequest.objects.filter(
                url='/post/{}'.format(p.slugged_title)
            )
        )

    view_context = {
        'page_title': '{} Analytics'.format(SITE_NAME),
        'post_list': post_list,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/analytics_index.html'.format(THEME),
        view_context,
    )


@user_passes_test(user_is_admin, login_url='/admin/login/')
def post(request, slugged_title):
    """View for /analytics/post/{post.slugged_title}."""
    p = Post.objects.get(slugged_title=slugged_title)
    page_requests = PageRequest.objects.filter(
        url='/post/{}'.format(p.slugged_title)
    )

    view_context = {
        'page_requests': page_requests,
        'page_title': '{} Analytics for POST: {}'.format(
            SITE_NAME, p.title
        ),
        'post': p,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/analytics_post.html'.format(THEME),
        view_context,
    )
