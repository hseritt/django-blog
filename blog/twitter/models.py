# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    message = models.CharField('Message', max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message
