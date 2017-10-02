# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Category, Post
from common.models import PageElement, SiteLink, RecommendedLink, SocialMediaLink
from .forms import ContactForm


tag_line = PageElement.objects.get(name='Tag Line', is_visible=True)
footer_text = PageElement.objects.get(name='Footer Text', is_visible=True)

def contact(request):

    if request.method == "GET":
        contact_form = ContactForm()
    elif request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponse(
                "<script>alert('Your message was successfully delivered.'); window.location.href='/';</script>"
            )

    category_list = Category.objects.filter(display=True)
    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    return render(
        request,
        'messaging_contact.html',
        {
            'category_list': category_list,
            'contact_form': contact_form,
            'footer_text': footer_text,
            'page_title': 'Contact',
            'recommended_link_list': recommended_link_list,
            'site_link_list': site_link_list,
            'social_media_link_list': social_media_link_list,
            'tag_line': tag_line,
        }
    )
