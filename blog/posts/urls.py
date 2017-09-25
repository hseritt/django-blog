from django.conf.urls import url, include
from django.contrib import admin
from .views import post_detail


urlpatterns = [
    url(
    	regex='^(?P<post_id>\d+)/$',
    	view=post_detail,
    	name='post_detail',
    ),
]
