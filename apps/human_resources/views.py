from django.shortcuts import render
from django.views.generic.base import View

from .models import Province, EmploymentIntention, WorkingIndustry, Family, PersonnelInformation


class HrInfoView(View):
    """人力资源"""

    def get(self, request):
        # 所有人员信息
        all_people = PersonnelInformation.objects.all()

        return render(request, 'hr_info.html', {'all_people': all_people})


class RealHrInfoView(View):
    """人力资源"""

    def get(self, request):

        return render(request, 'hr_info.html')