# -*- coding: utf-8 -*-
"""Django admin settings for analytics app.
"""
from __future__ import unicode_literals

from django.contrib import admin
from .models import PageRequest


class PageRequestAdmin(admin.ModelAdmin):
    readonly_fields = ['request_date',]

admin.site.register(PageRequest, PageRequestAdmin)
