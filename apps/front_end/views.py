from django.shortcuts import render
from django.views.generic.base import View


class BaseInfoView(View):
    """基础设施"""

    def get(self, request):
        return render(request, 'base_info.html')


class IndexView(View):
    """首页"""

    def get(self, request):
        return render(request, 'index.html', {})


class IndustryInfoView(View):
    """产业发展"""

    def get(self, request):
        return render(request, 'industry_info.html')


class InfoView(View):
    """info"""

    def get(self, request):
        return render(request, 'info.html')


class LiveInfoView(View):
    """扶贫民生"""

    def get(self, request):
        return render(request, 'live_info.html')


class LoginView(View):
    """登录"""

    def get(self, request):
        return render(request, 'login.html')


class PartyInfoView(View):
    """基层组织"""

    def get(self, request):
        return render(request, 'party_info.html')
