"""gradutework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns
from django.contrib import admin
from homework.views import login, index, register, logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    (r'^admin/', include(admin.site.urls)),
    (r'^login/$', login),
    (r'^index/$', index),
    (r'^logout/$', logout),
    (r'^register/$', register),
    (r'^captcha/', include('captcha.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)