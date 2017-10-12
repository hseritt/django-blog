# -*- coding: utf-8 -*-
"""Django admin settings for messaging app.
"""
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact


admin.site.register(Contact)
