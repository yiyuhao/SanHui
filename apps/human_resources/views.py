import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Province, EmploymentIntention, WorkingIndustry, Family, PersonnelInformation


class HrInfoView(View):
    """人力资源"""

    def get(self, request):
        # 所有人员信息
        all_people = PersonnelInformation.objects.all()

        return render(request, 'hr_info.html', {'all_people': all_people})


class AjaxGetHrInfoView(View):
    """ajax获取人力资源信息"""

    def get(self, request):
        all_people = PersonnelInformation.objects.all()
        all_people = serializers.serialize('json', all_people)

        return HttpResponse(all_people, content_type='application/json')
