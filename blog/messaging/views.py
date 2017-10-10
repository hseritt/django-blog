# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Post
from common.contexts import get_common_view_context
from .forms import ContactForm
from analytics.models import PageRequest

def contact(request):

    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    else:
        http_referer = ''

    pr = PageRequest.objects.create(
        name='Contact',
        url='/contact/',
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        pr.referer = http_referer
        pr.save()

    if request.method == "GET":
        contact_form = ContactForm()
    elif request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponse(
                "<script>alert('Your message was successfully delivered.'); window.location.href='/';</script>"
            )

    view_context = {
        'contact_form': contact_form,
        'page_title': 'Contact',
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        'messaging_contact.html',
        view_context,
    )
