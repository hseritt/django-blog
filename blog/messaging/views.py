# -*- coding: utf-8 -*-
"""Views module for messaging app.
"""
from __future__ import unicode_literals

from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from blog.settings import THEME
from lib.util import get_http_referer
from common.contexts import get_common_view_context
from analytics.models import PageRequest
from .forms import ContactForm
from .models import Prospect


def contact(request):
    """View for /contact/"""
    http_referer = get_http_referer(request)

    page_request = PageRequest.objects.create(
        name='Contact',
        url='/contact/',
        ip_addr=request.META['REMOTE_ADDR'],
    )

    if http_referer:
        page_request.referer = http_referer
        page_request.save()

    if request.method == "GET":
        contact_form = ContactForm()
    elif request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            c = contact_form.save()

            try:
                Prospect.objects.create(
                    sender_name=c.sender_name,
                    email=c.sender_email
                )
            except IntegrityError:
                pass

            return HttpResponse(
                "<script>alert('Your message was successfully delivered.'); "
                "window.location.href='/';</script>"
            )

    view_context = {
        'contact_form': contact_form,
        'page_title': 'Contact',
    }

    view_context.update(get_common_view_context())

    return render(
        request,
        '{}/messaging_contact.html'.format(THEME),
        view_context,
    )
