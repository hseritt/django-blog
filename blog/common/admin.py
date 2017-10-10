# -*- coding: utf-8 -*-
"""
Django admin settings for common app.
"""
from __future__ import unicode_literals

from django.contrib import admin
from .models import PageElement, RecommendedLink, SiteLink, SocialMediaLink


admin.site.register(RecommendedLink)
admin.site.register(SiteLink)
admin.site.register(SocialMediaLink)
admin.site.register(PageElement)
