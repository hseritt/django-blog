# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User)
    content = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __unicode__(self):
        return self.title
