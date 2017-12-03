from datetime import datetime

from django.db import models


class Province(models.Model):
    name = models.CharField(verbose_name='省份(直辖市)', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200, null=True, blank=True)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '省份(城市)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PersonnelInformation(models.Model):
    group = models.CharField(verbose_name='组数', max_length=4)
    name = models.CharField(verbose_name='姓名', max_length=20)
    gender = models.CharField(verbose_name='性别', choices=(('male', '男'), ('female', '女')))
    birthday = models.DateField(verbose_name='出生年月', null=True, blank=True)
    permanent_residence = models.ForeignKey(Province, verbose_name='常住地')
    degree_of_education = models.CharField(verbose_name='文化程度', max_length=20)
    political_status = models.CharField(verbose_name='政治面貌', max_length=20)
    school_major_field = models.CharField(verbose_name='在读院校和专业', max_length=50)
    employment_intention = models.CharField(verbose_name='就业意向', max_length=50)
    is_village_cadres = models.CharField(verbose_name='是否为村干部及职位', max_length=30, default='否')
    is_village_backup_cadres = models.CharField(verbose_name='是否为村后备干部及职位', max_length=30, default='否')
    is_local_talent = models.CharField(verbose_name='是否为乡土人才及技能', max_length=30, default='否')
    is_career_creating_talent = models.CharField(verbose_name='是否创业人才及创业方向', max_length=30, default='否')
    working_place = models.CharField(verbose_name='务工地点', max_length=30)
    working_years = models.CharField(verbose_name='务工年限', max_length=30)
    working_position = models.CharField(verbose_name='务工职位', max_length=30)
    phone_num = models.CharField(verbose_name='联系方式', max_length=11, null=True, blank=True)
    is_disabled_people = models.CharField(verbose_name='是否残疾', choices=(('yes', '是'), ('no', '否')))
    is_basic_living_allowances = models.CharField(verbose_name='是否低保', choices=(('yes', '是'), ('no', '否')))
    is_rural_social_endowment_insurance = models.CharField(verbose_name='是否农保', choices=(('yes', '是'), ('no', '否')))
    is_medical_insurance = models.CharField(verbose_name='是否参加医保', choices=(('yes', '是'), ('no', '否')))

