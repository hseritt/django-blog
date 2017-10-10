# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone
from posts.models import Category, Post
from common.models import PageElement


class PostsViewsTestCase(TestCase):

    def create_test_post(self):

        admin_user = User.objects.create(
            username='admin',
            email='admin@localhost',
        )

        category = Category(
            name='TestCategory',
        )
        category.save()
        
        self.post = Post(
            title='This is my title',
            author=admin_user,
            content='Some content',
            published=timezone.now(),
            is_published=True,
            slugged_title='this-is-my-title',
        )
        self.post.save()
        self.post.categories.add(category)
        self.post.save()

    def setUp(self):
        PageElement.objects.create(name='Tag Line', text='some text')
        PageElement.objects.create(name='Footer Text', text='some text')
        self.create_test_post()

    def test_post_get(self):
        client = Client()
        response = client.get(
            '/post/{}/'.format(self.post.slugged_title)
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post.title in response.content)

    def test_post_filtered(self):
        client = Client()
        for category in self.post.categories.all():
            url = '/post/filter/?category_name={}'.format(category.name)
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.post.title in response.content)
