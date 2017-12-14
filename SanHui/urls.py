"""SanHui URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import xadmin

from front_end.views import IndexView, LoginView, BaseInfoView, IndustryInfoView, InfoView, PartyInfoView, \
    LiveInfoView
from human_resources.views import HrInfoView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^hr_info/', HrInfoView.as_view(), name='hr_info'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^base_info/', BaseInfoView.as_view(), name='base_info'),
    url(r'^industry_info/', IndustryInfoView.as_view(), name='industry_info'),
    url(r'^info/', InfoView.as_view(), name='info'),
    url(r'^party_info/', PartyInfoView.as_view(), name='party_info'),
    url(r'^live_info/', LiveInfoView.as_view(), name='live_info'),
]
