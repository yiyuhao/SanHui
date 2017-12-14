from django.shortcuts import render
from django.views.generic.base import View


class HrInfoView(View):
    """人力资源"""

    def get(self, request):
        return render(request, 'hr_info.html')


class RealHrInfoView(View):
    """人力资源"""

    def get(self, request):

        return render(request, 'hr_info.html')