"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from common.views import about, index
from messaging.views import contact


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^analytics/', include('analytics.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^post/', include('posts.urls')),
    url(
        regex=r'^$',
        view=index,
        name='common_index',
    ),
    url(
        regex=r'^about/$',
        view=about,
        name='common_about',
    ),
    url(
        regex=r'^contact/$',
        view=contact,
        name='messaging_contact'
    )
]
