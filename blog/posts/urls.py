"""
Urls patterns for posts app.
"""
from django.conf.urls import url
from .views import post_detail, posts_filtered


urlpatterns = [
    url(
        regex=r'^filter/',
        view=posts_filtered,
        name='posts_filtered',
    ),
    url(
        regex=r'^(?P<slugged_title>.+)/$',
        view=post_detail,
        name='post_detail',
    ),
]
