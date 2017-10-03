# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=50, unique=True)
    display = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = (
            ('name', 'parent'),
        )

    def __unicode__(self):
        return self.name


class Post(models.Model):
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
        return markdownify(self.content)

    def __unicode__(self):
        return self.title
