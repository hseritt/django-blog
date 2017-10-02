# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):

    sender_name = models.CharField('Your Name', max_length=50)
    sender_email = models.EmailField('Your Email Address')
    message = models.TextField('Message')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'From {} at {}'.format(self.sender_name, self.created)
