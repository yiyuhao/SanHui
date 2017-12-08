from datetime import datetime

from django.db import models


class Province(models.Model):
    name = models.CharField(verbose_name='省份(直辖市)', max_length=20)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '省份(城市)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class EmploymentIntention(models.Model):
    name = models.CharField(verbose_name='专业方向', max_length=20)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '专业方向'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Family(models.Model):
    householder = models.CharField(verbose_name='户主', max_length=20)
    is_poor_households = models.CharField(verbose_name='是否为贫困户', max_length=3, choices=(
        ('yes', '是'), ('no', '否')), default='no')
    causes_of_poverty = models.CharField(verbose_name='致贫原因', max_length=100, null=True, blank=True)
    per_capita_arable_land_area = models.FloatField(verbose_name='人均耕地面积(亩)', default=0)
    per_capita_woodland_area = models.FloatField(verbose_name='人均林地面积(亩)', default=0)
    per_capita_circulation_area = models.FloatField(verbose_name='人均已流转面积(亩)', default=0)
    annual_income = models.IntegerField(verbose_name='年收入(元)', default=0)
    medical_expenditure = models.IntegerField(verbose_name='医疗支出(元)', default=0)
    education_expenditure = models.IntegerField(verbose_name='教育支出(元)', default=0)
    living_production_expenditure = models.IntegerField(verbose_name='生活生产支出(元)', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    remarks = models.CharField(verbose_name='备注', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = '户(家庭)信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '户主: ' + self.householder


class PersonnelInformation(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    group = models.CharField(verbose_name='组数', max_length=4)
    gender = models.CharField(verbose_name='性别', max_length=6, choices=(
        ('male', '男'), ('female', '女')), default='male')
    birthday = models.DateField(verbose_name='出生年月', null=True, blank=True)
    permanent_residence = models.ForeignKey(Province, verbose_name='常住地')
    home = models.ForeignKey(Family, verbose_name='所在户(户主)', null=True, blank=True)

    degree_of_education = models.CharField(verbose_name='文化程度', max_length=5, default='cz', choices=(
        ('cz', '初中及以下'), ('gz', '高中'), ('dz', '大专'), ('bk', '本科'), ('ss', '硕士'), ('bs', '博士')))
    political_status = models.CharField(verbose_name='政治面貌', max_length=6, default='qz', choices=(
        ('qz', '群众'), ('ty', '团员'), ('rdjjfz', '入党积极分子'), ('ybdy', '预备党员'), ('zsdy', '正式党员')))
    school_major_field = models.CharField(verbose_name='在读院校和专业', max_length=50, null=True, blank=True)
    employment_intention = models.ForeignKey(EmploymentIntention, verbose_name='就业意向', null=True, blank=True)

    is_village_cadres = models.CharField(verbose_name='是否为村干部及职位', max_length=30, default='否')
    is_village_backup_cadres = models.CharField(verbose_name='是否为村后备干部', max_length=3, choices=(
        ('yes', '是'), ('no', '否')), default='no')
    is_local_talent = models.CharField(verbose_name='是否为乡土人才及技能', max_length=30, default='否')
    is_career_creating_talent = models.CharField(verbose_name='是否创业人才及创业方向', max_length=30, default='否')

    working_place = models.CharField(verbose_name='务工地点', max_length=30, null=True, blank=True)
    working_years = models.CharField(verbose_name='务工年限', max_length=4, null=True, blank=True, choices=(
        ('1', '1年以下'), ('1to5', '1-5年'), ('5', '5年以上')), default='1to5')
    working_industry = models.CharField(verbose_name='务工行业', max_length=30, null=True, blank=True)
    working_salary = models.CharField(verbose_name='务工年收入', max_length=5, null=True, blank=True, choices=(
        ('5', '5万以下'), ('5to8', '5-8万'), ('8to12', '8-12万'), ('12', '12万以上')), default='5')
    working_position = models.CharField(verbose_name='务工职位', max_length=30, null=True, blank=True)

    phone_num = models.CharField(verbose_name='联系方式', max_length=11, null=True, blank=True)
    health_status = models.CharField(verbose_name='身体状况', max_length=9, choices=(
        ('jk', '健康'), ('hyjb', '患有疾病'), ('cj', '残疾')), default='jk')
    is_basic_living_allowances = models.CharField(verbose_name='最低保障', max_length=3, choices=(
        ('db', '低保'), ('wb', '五保'), ('w', '无')), default='w')
    is_rural_social_endowment_insurance = models.CharField(verbose_name='是否农保', max_length=3, choices=(
        ('yes', '是'), ('no', '否')), default='yes')
    is_medical_insurance = models.CharField(verbose_name='是否参加医保', max_length=3, choices=(
        ('yes', '是'), ('no', '否')), default='yes')
    is_social_security = models.CharField(verbose_name='是否参加社保', max_length=3, choices=(
        ('yes', '是'), ('no', '否')), default='yes')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    remarks = models.CharField(verbose_name='备注', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = '人员信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
