# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BlogLink(models.Model):
    name = models.CharField(max_length=35, unique=True)
    url = models.TextField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SiteLink(BlogLink):
    class Meta:
        verbose_name = 'Site Link'
        verbose_name_plural = 'Site Links'
    def __unicode__(self):
        return 'Site Link: {}'.format(self.name)


class RecommendedLink(BlogLink):
    class Meta:
        verbose_name = 'Recommended Link'
        verbose_name_plural = 'Recommended Links'
    def __unicode__(self):
        return 'Recommended Link: {}'.format(self.name)


class SocialMediaLink(BlogLink):
    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = 'Social Media Links'
    def __unicode__(self):
        return 'Social Media Link: {}'.format(self.name)
