"""URLs router configs for analytics app."""
from django.conf.urls import url
from .views import index, post


urlpatterns = [
    url(
        regex=r'^$',
        view=index,
        name='analytics_index',
    ),
    url(
    	regex=r'^post/(?P<slugged_title>.+)/$',
    	view=post,
    	name='analytics_post',
    ),
]
