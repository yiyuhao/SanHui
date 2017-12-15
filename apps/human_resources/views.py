import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Province, EmploymentIntention, WorkingIndustry, Family, PersonnelInformation
from .adminx import PersonnelInformationAdmin
from utils.json import model_to_json


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
        all_people_json = model_to_json(all_people, PersonnelInformationAdmin.list_display)

        return HttpResponse(all_people_json, content_type='application/json')
