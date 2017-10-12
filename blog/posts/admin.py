# -*- coding: utf-8 -*-
"""Django admin settings for analytics app.
"""
from __future__ import unicode_literals

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category

class PostModelAdmin(MarkdownxModelAdmin):
    """Admin model including markdown field for textarea."""
    prepopulated_fields = {'slugged_title': ('title',)}

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
