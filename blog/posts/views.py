# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.settings import SITE_NAME
from .models import Category, Post
from common.models import SiteLink, RecommendedLink, SocialMediaLink


def post_detail(request, post_id):

    post = Post.objects.get(pk=post_id)
    category_list = Category.objects.filter(display=True)
    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    return render(
        request,
        'posts_post.html',
        {
            'category_list': category_list,
            'page_title': 'Post: {}'.format(post.title),
            'post': post,
            'recommended_link_list': recommended_link_list,
            'site_link_list': site_link_list,
            'social_media_link_list': social_media_link_list,
        }
    )


def posts_filtered(request):

    filt = request.GET['category_name']

    category = Category.objects.get(name=filt)

    post_list = Post.objects.filter(
        categories__in=[category,]
    ).order_by('-created')

    category_list = Category.objects.filter(display=True)

    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    return render(
        request,
        'common_index.html',
        {
            'category_list': category_list,
            'page_title': SITE_NAME,
            'post_list': post_list,
            'recommended_link_list': recommended_link_list,
            'site_link_list': site_link_list,
            'social_media_link_list': social_media_link_list,
        },
    )
