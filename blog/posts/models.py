# -*- coding: utf-8 -*-
"""Models module for posts app.
"""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    """Category for posts."""
    name = models.CharField(max_length=50, unique=True)
    display = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """Blog posts"""
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User)
    content = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True, editable=True)
    published = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    slugged_title = models.SlugField(max_length=100, unique=True)

    @property
    def formatted_markdown(self):
        """For use with markdown fields."""
        return markdownify(self.content)

    def __unicode__(self):
        return self.title
