# -*- coding: utf-8 -*-
"""Views module for analytics app.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from blog.settings import SITE_NAME
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

    for post in post_list:
        post.hits = len(
            PageRequest.objects.filter(
                url='/post/{}'.format(post.slugged_title)
            )
        )

    view_context = {
        'page_title': '{} Analytics'.format(SITE_NAME),
        'post_list': post_list,
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        'analytics_index.html',
        view_context,
    )
