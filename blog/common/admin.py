# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import RecommendedLink, SiteLink, SocialMediaLink


admin.site.register(RecommendedLink)
admin.site.register(SiteLink)
admin.site.register(SocialMediaLink)
