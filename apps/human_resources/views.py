import json

from django.apps import apps
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

        # 获取所有筛选标签
        # [
        #     ['group', '组数', (('1', '一组'),
        #                        ('2', '二组'), ...)],
        #     ['gender', '性别', (('male', '男'),
        #                         ('female', '女'))],
        #     ...
        # ]
        filter_fields = []
        model_fields = apps.get_model('human_resources', 'PersonnelInformation')._meta.fields
        for field in model_fields:
            key, key_cn, choices = field.attname, field._verbose_name, field.choices
            if choices:
                pass
            elif key_cn == '常住地':
                obj = Province.objects.all()
                choices = tuple([(o.filter_name, o.name) for o in obj])
            elif key_cn == '就业意向':
                obj = EmploymentIntention.objects.all()
                choices = tuple([(o.filter_name, o.name) for o in obj])
            elif key_cn == '务工行业':
                obj = WorkingIndustry.objects.all()
                choices = tuple([(o.filter_name, o.name) for o in obj])
            else:
                continue
            filter_fields.append((key, key_cn, choices))

        return render(request, 'hr_info.html', {'all_people': all_people,
                                                'filter_fields': filter_fields})


class AjaxGetHrInfoView(View):
    """ajax获取人力资源信息"""

    def get(self, request):
        all_people = PersonnelInformation.objects.all()

        # 筛选参数及值
        filter_params = {}
        for k, v in request.GET.items():
            if not k.startswith('_'):
                # 处理外键如working_industry_id  改为查询working_industry__filter_name__exact
                if k[-3:] == '_id':
                    k = k[:-3] + '__filter_name__exact'
                filter_params[k] = v

        # 后台筛选
        all_people = all_people.filter(**filter_params)

        all_people_json = model_to_json(all_people, PersonnelInformationAdmin.list_display)

        return HttpResponse(all_people_json, content_type='application/json')
