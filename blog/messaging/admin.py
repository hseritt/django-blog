# -*- coding: utf-8 -*-
"""Django admin settings for messaging app.
"""
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact, Prospect


class ProspectAdmin(admin.ModelAdmin):
    """Admin config for Prospect model."""
    readonly_fields = [
        'created'
    ]


admin.site.register(Contact)
admin.site.register(Prospect, ProspectAdmin)
