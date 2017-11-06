# -*- coding: utf-8 -*-
"""Models module for common app.
"""
from __future__ import unicode_literals

from django.db import models


class BlogLink(models.Model):
    """
    Abstract model for different types of links used.
    """
    name = models.CharField(max_length=35, unique=True)
    url = models.TextField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SiteLink(BlogLink):
    """Links like home, contact, about, etc."""
    class Meta:
        verbose_name = 'Site Link'
        verbose_name_plural = 'Site Links'

    def __unicode__(self):
        return 'Site Link: {}'.format(self.name)


class RecommendedLink(BlogLink):
    """External links outside this blog."""
    class Meta:
        verbose_name = 'Recommended Link'
        verbose_name_plural = 'Recommended Links'

    def __unicode__(self):
        return 'Recommended Link: {}'.format(self.name)


class SocialMediaLink(BlogLink):
    """Social media links."""
    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = 'Social Media Links'

    def __unicode__(self):
        return 'Social Media Link: {}'.format(self.name)


class PageElement(models.Model):
    """Parts of pages."""
    name = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Page Element'
        verbose_name_plural = 'Page Elements'

    def __unicode__(self):
        return self.name
