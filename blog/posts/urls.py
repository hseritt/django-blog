from django.conf.urls import url, include
from django.contrib import admin
from .views import post_detail, posts_filtered


urlpatterns = [
    url(
    	regex=r'^(?P<slugged_title>.+)/$',
    	view=post_detail,
    	name='post_detail',
    ),
    url(
    	regex=r'^filter/',
    	view=posts_filtered,
    	name='posts_filtered',
    ),
]
