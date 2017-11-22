from django.shortcuts import render
from django.views.generic.base import View

from .models import Village


class IndexView(View):
    """首页"""

    def get(self, request):
        san_hui = Village.objects.first()
        return render(request, 'index.html', {'village_name': san_hui.name,
                                              'people_nums': san_hui.people_nums})


class InfrastructureView(View):
    """基础设施详情页"""

    def get(self, request):
        return render(request, 'info.html', {})
