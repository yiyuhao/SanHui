import xadmin

from .models import Province, EmploymentIntention, PersonnelInformation


class ProvinceAdmin:
    list_display = ['name', 'add_time']
    list_filter = list_display
    search_fields = ['name']


class EmploymentIntentionAdmin:
    list_display = ['name', 'add_time']
    list_filter = list_display
    search_fields = ['name']


class PersonnelInformationAdmin:
    list_display = ['name', 'group', 'gender', 'birthday', 'permanent_residence', 'degree_of_education',
                    'political_status', 'school_major_field', 'employment_intention', 'is_village_cadres',
                    'is_village_backup_cadres', 'is_local_talent', 'is_career_creating_talent', 'working_place',
                    'working_years', 'working_position', 'phone_num', 'health_status', 'is_basic_living_allowances',
                    'is_rural_social_endowment_insurance', 'is_medical_insurance', 'add_time']

    list_filter = list_display
    search_fields = ['name', 'group', 'school_major_field', 'working_industry', 'working_position', 'remarks']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(EmploymentIntention, EmploymentIntentionAdmin)
xadmin.site.register(PersonnelInformation, PersonnelInformationAdmin)
