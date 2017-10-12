# -*- coding: utf-8 -*-
"""Models for analytics app.
"""
from __future__ import unicode_literals

from django.db import models

class PageRequest(models.Model):
    """PageRequest model for user page requests.
    """
    name = models.CharField('Name', max_length=255)
    url = models.CharField('URL', max_length=255)
    request_date = models.DateTimeField('Request Date', auto_now_add=True)
    ip_addr = models.CharField('IP Address of Request', max_length=255)
    referer = models.CharField('Referer', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Page Request'
        verbose_name_plural = 'Page Requests'

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.request_date)
