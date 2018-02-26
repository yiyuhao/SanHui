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

from front_end.views import IndexView, LoginView, FarmingView, HealthView, HistoryView, NaturalView, TourView, \
    LiveInfoView
from human_resources.views import HrInfoView, AjaxGetHrInfoView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^farming/', FarmingView.as_view(), name='farming'),
    url(r'^health/', HealthView.as_view(), name='health'),
    url(r'^history/', HistoryView.as_view(), name='history'),
    url(r'^natural/', NaturalView.as_view(), name='natural'),
    url(r'^tour/', TourView.as_view(), name='tour'),
    url(r'^live_info/', LiveInfoView.as_view(), name='live_info'),

    url(r'^hr_info/', HrInfoView.as_view(), name='hr_info'),
    url(r'^login/', LoginView.as_view(), name='login'),

    url(r'^get_hr_info/', AjaxGetHrInfoView.as_view(), name='get_hr_info'),
]
