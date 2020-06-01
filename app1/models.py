from django.db import models


class MeetingApp(models.Model):
    status_CHOICES = (
        ('1', '已签到'),  # 1为数据库显示，已签到为后台显示
        ('0', '未签到')
    )
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='姓名')
    workplace = models.CharField(max_length=30, blank=True, null=True, verbose_name='所属单位')
    mobile = models.CharField(primary_key=True, max_length=255, unique=True, verbose_name='联系电话')
    email = models.CharField(max_length=25, blank=True, null=True, unique=True, verbose_name='邮箱地址')
    demand = models.TextField(max_length=500, blank=True, null=True, verbose_name='食宿要求')
    title = models.CharField(max_length=25, blank=True, null=True, verbose_name='报告题目')
    abstract = models.TextField(max_length=400, blank=True, null=True, verbose_name='报告摘要')
    sign = models.CharField(max_length=5, choices=status_CHOICES, default="0", verbose_name='签到状态')

    class Meta:
        managed = True
        verbose_name_plural = '参会名单'
