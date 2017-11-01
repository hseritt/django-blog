# -*- coding: utf-8 -*-
"""Models module for messaging app.
"""
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    """Contact or message model."""
    sender_name = models.CharField('Your Name', max_length=50)
    sender_email = models.EmailField('Your Email Address')
    message = models.TextField('Message')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'From {} at {}'.format(self.sender_name, self.created)


class Prospect(models.Model):
    """Used for collection of prospect emails and contact information."""
    sender_name = models.CharField('Full Name', max_length=50)
    email = models.EmailField('Email Address', unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} / {}'.format(self.sender_name, self.email)
