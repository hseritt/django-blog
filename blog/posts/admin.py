# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from .models import Post


admin.site.register(Post, MarkdownxModelAdmin)
