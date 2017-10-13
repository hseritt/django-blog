"""URLs router configs for analytics app."""
from django.conf.urls import url, include
from .views import index


urlpatterns = [
    url(
        regex=r'^$',
        view=index,
        name='analytics_index',
    ),
]
