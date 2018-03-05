from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect


from .forms import LoginForm


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = AbstractUser.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None


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

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 尝试认证用户并返回user
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('hr_info'))
            # 用户名密码错误
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
        # 表单字段未验证通过
        return render(request, 'login.html', {'login_form': login_form})


class NaturalView(View):
    """自然环境"""

    def get(self, request):
        return render(request, 'natural.html')


class TourView(View):
    """康养旅游"""

    def get(self, request):
        return render(request, 'tour.html')
