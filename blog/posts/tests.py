# -*- coding: utf-8 -*-
"""Tests module for posts app.
"""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone
from posts.models import Category, Post
from common.models import PageElement


class PostsViewsTestCase(TestCase):
    """Test case for Posts views."""
    def create_admin_user(self):
        """Create a test admin user."""
        self.admin_user = User.objects.create(
            username='admin',
            email='admin@localhost',
        )

    def create_test_category(self):
        """Create a test category."""
        self.category = Category(
            name='TestCategory',
        )
        self.category.save()

    def create_test_post(self):
        """Create a test post for use with other tests."""
        self.post = Post(
            title='This is my title',
            author=self.admin_user,
            content='Some content',
            published=timezone.now(),
            is_published=True,
            slugged_title='this-is-my-title',
        )
        self.post.save()
        self.post.categories.add(self.category)
        self.post.save()

    def setUp(self):
        """ setup """
        self.create_admin_user()
        self.create_test_category()
        PageElement.objects.create(name='Tag Line', text='some text')
        PageElement.objects.create(name='Footer Text', text='some text')
        self.create_test_post()

    def test_post_get(self):
        """Test GET /post/{}"""
        client = Client()
        response = client.get(
            '/post/{}/'.format(self.post.slugged_title)
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post.title in response.content)

    def test_post_filtered(self):
        """Test GET /post/filter/?category_name={}"""
        client = Client()
        for category in self.post.categories.all():
            url = '/post/filter/?category_name={}'.format(category.name)
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.post.title in response.content)

    def test_post_is_published(self):
        """Test that is_published is being used as it should."""
        # self.create_test_post()
        post = Post.objects.get(title='This is my title')
        client = Client()
        response = client.get(
            '/',
            follow=True
        )
        self.assertTrue('This is my title' in response.content)
        post.is_published = False
        post.save()

        response = client.get(
            '/',
            follow=True
        )
        self.assertFalse('This is my title' in response.content)
