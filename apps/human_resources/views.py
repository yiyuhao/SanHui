import json

from django.apps import apps
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Province, EmploymentIntention, WorkingIndustry, Family, PersonnelInformation
from .adminx import PersonnelInformationAdmin
from utils.json import model_to_json
from utils.function import order_by_occur_nums
from SanHui.settings import PAGINATION_SETTINGS

from utils.mixin_utils import LoginRequiredMixin


class HrInfoView(LoginRequiredMixin, View):
    """人力资源"""

    def get(self, request):
        # 所有人员信息
        all_people = PersonnelInformation.objects.all()

        # 数量
        num_of_personnel = all_people.count()

        # 获取top8常住地/就业意向/务工行业
        nums = 8
        province_ids = [p.permanent_residence.id for p in all_people if p.permanent_residence is not None]
        province_ids = order_by_occur_nums(province_ids)
        provinces = Province.objects.filter(id__in=province_ids)[:nums]

        intention_ids = [p.employment_intention.id for p in all_people if p.employment_intention is not None]
        intention_ids = order_by_occur_nums(intention_ids)
        intentions = EmploymentIntention.objects.filter(id__in=intention_ids)[:nums]

        industry_ids = [p.working_industry.id for p in all_people if p.working_industry is not None]
        industry_ids = order_by_occur_nums(industry_ids)
        industries = WorkingIndustry.objects.filter(id__in=industry_ids)[:nums]

        # 取第一页
        per_page = PAGINATION_SETTINGS.get('PER_PAGE', 10)
        paginator = Paginator(all_people, per_page)
        p = paginator.page(1)

        all_people = p.object_list

        # 需要返回给前端总页数
        pages_num = paginator.num_pages

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
                choices = tuple([(o.filter_name, o.name) for o in provinces])
            elif key_cn == '就业意向':
                choices = tuple([(o.filter_name, o.name) for o in intentions])
            elif key_cn == '务工行业':
                choices = tuple([(o.filter_name, o.name) for o in industries])
            else:
                continue
            filter_fields.append((key, key_cn, choices))

        return render(request, 'hr_info.html', {'all_people': all_people,
                                                'filter_fields': filter_fields,
                                                'pages_num': pages_num,
                                                'num_of_personnel': num_of_personnel,})


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

        # 页数
        page = filter_params.pop('page', 1)

        # 后台筛选
        all_people = all_people.filter(**filter_params)

        # 分页
        per_page = PAGINATION_SETTINGS.get('PER_PAGE', 10)
        paginator = Paginator(all_people, per_page)
        try:
            p = paginator.page(page)
        except PageNotAnInteger:
            p = paginator.page(1)
        except EmptyPage:
            p = paginator.page(paginator.num_pages)
            p.object_list = []
        # 人力资源列表进行分页
        all_people = p.object_list

        all_people_json = model_to_json(all_people, PersonnelInformationAdmin.list_display)

        return HttpResponse(all_people_json, content_type='application/json')
