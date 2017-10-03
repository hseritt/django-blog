# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from blog.settings import SITE_NAME
from posts.models import Post
from common.contexts import common_view_context
from .forms import ContactForm


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

    view_context = {
        'contact_form': contact_form,
        'page_title': 'Contact',
    }

    view_context.update(common_view_context)

    return render(
        request,
        'messaging_contact.html',
        view_context,
    )
