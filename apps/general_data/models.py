from datetime import datetime

from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=100, verbose_name='村名')
    people_nums = models.IntegerField(verbose_name='人口数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '村数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
