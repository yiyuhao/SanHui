import xadmin

from .models import Province, EmploymentIntention, Family, PersonnelInformation, WorkingIndustry


class ProvinceAdmin:
    list_display = ['filter_name', 'name', 'add_time']
    list_filter = list_display
    search_fields = ['name']


class EmploymentIntentionAdmin:
    list_display = ['filter_name', 'name', 'add_time']
    list_filter = list_display
    search_fields = ['name']


class WorkingIndustryAdmin:
    list_display = ['filter_name', 'name', 'add_time']
    list_filter = list_display
    search_fields = ['name']


class FamilyAdmin:
    list_display = ['householder', 'is_poor_households', 'causes_of_poverty', 'per_capita_arable_land_area',
                    'per_capita_woodland_area', 'per_capita_circulation_area', 'annual_income', 'medical_expenditure',
                    'education_expenditure', 'living_production_expenditure', 'add_time', 'remarks']
    list_filter = list_display
    search_fields = ['householder', 'causes_of_poverty', 'remarks']


class PersonnelInformationAdmin:
    list_display = ['name', 'group', 'gender', 'birthday', 'permanent_residence', 'home', 'degree_of_education',
                    'political_status', 'school_major_field', 'employment_intention', 'is_village_cadres',
                    'is_village_backup_cadres', 'is_local_talent', 'is_career_creating_talent', 'working_place',
                    'working_years', 'working_industry', 'working_salary', 'working_position', 'phone_num',
                    'health_status', 'is_basic_living_allowances', 'is_rural_social_endowment_insurance',
                    'is_medical_insurance', 'is_social_security', 'add_time', 'remarks']

    list_filter = list_display
    search_fields = ['name', 'group', 'school_major_field', 'working_industry', 'working_position', 'remarks']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(EmploymentIntention, EmploymentIntentionAdmin)
xadmin.site.register(Family, FamilyAdmin)
xadmin.site.register(PersonnelInformation, PersonnelInformationAdmin)
xadmin.site.register(WorkingIndustry, WorkingIndustryAdmin)
