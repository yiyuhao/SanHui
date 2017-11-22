from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    """首页"""

    def get(self, request):
        return render(request, 'index.html', {})
