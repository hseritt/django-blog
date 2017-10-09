# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PageRequest(models.Model):

    name = models.CharField('Name', max_length=50)
    url = models.CharField('URL', max_length=255)
    req_dt = models.DateTimeField('Request Date', auto_now_add=True)
    ip_addr = models.CharField('IP Address of Request', max_length=16)
    referer = models.CharField('Referer', max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.req_dt)
