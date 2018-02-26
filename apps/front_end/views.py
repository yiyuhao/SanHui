from django.shortcuts import render
from django.views.generic.base import View


class FarmingView(View):
    """现代农业"""

    def get(self, request):
        return render(request, 'farming.html')


class HealthView(View):
    """医疗卫生"""

    def get(self, request):
        return render(request, 'health.html')


class HistoryView(View):
    """历史文化"""

    def get(self, request):
        return render(request, 'history.html')


class IndexView(View):
    """首页"""

    def get(self, request):
        return render(request, 'index.html')


class LiveInfoView(View):
    """脱贫奔康"""

    def get(self, request):
        return render(request, 'live_info.html')


class LoginView(View):
    """登录"""

    def get(self, request):
        return render(request, 'login.html')


class NaturalView(View):
    """自然环境"""

    def get(self, request):
        return render(request, 'natural.html')


class TourView(View):
    """康养旅游"""

    def get(self, request):
        return render(request, 'tour.html')
