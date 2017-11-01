# -*- coding: utf-8 -*-
"""Tests module for messaging app.
"""
from __future__ import unicode_literals

from django.test import Client, TestCase
from common.models import PageElement
from messaging.models import Contact, Prospect


class MessagingViewsTestCase(TestCase):
    """Test for all Messaging views."""
    def setUp(self):
        """ setup """
        PageElement.objects.create(name='Tag Line', text='some text')
        PageElement.objects.create(name='Footer Text', text='some text')

    def test_contact_get(self):
        """Test for GET /contact/"""
        client = Client()
        response = client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Your Name:' in response.content)
        self.assertTrue('Your Email Address:' in response.content)
        self.assertTrue('Message:' in response.content)

    def test_contact_post(self):
        """Test for POST /contact/"""
        client = Client()
        client.post(
            '/contact/',
            {
                'sender_name': 'Bill',
                'sender_email': 'bill@localhost',
                'message': 'this is a message'
            },
            follow=True
        )
        self.assertTrue(Contact.objects.get(sender_name='Bill'))
        self.assertTrue(Prospect.objects.get(email='bill@localhost'))
        self.test_contact_get()
