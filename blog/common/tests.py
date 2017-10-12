# -*- coding: utf-8 -*-
"""Unit tests for common app.
"""
from __future__ import unicode_literals

from django.test import Client, TestCase
from common.models import PageElement

class CommonViewsTestCase(TestCase):
    """Test cases for all common views."""

    def setUp(self):
        """ setup """
        PageElement.objects.create(name='Tag Line', text='some text')
        PageElement.objects.create(name='Footer Text', text='some text')

    def test_index_get(self):
        """Tests GET of /"""
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dev.prodigi.us' in response.content)

    def test_about_get(self):
        """Tests GET of /about/"""
        client = Client()
        response = client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('About' in response.content)
