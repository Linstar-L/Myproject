from django.conf import settings
from django.db import models


# from newuser.models import NewUser


# Create your models here.
class MyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女")
    )
    EDUCATION_CHOICES = (
        ('高中', '高中'),
        ('中专', '中专'),
        ('大专', '大专'),
        ('本科', '本科'),
        ('硕士', '硕士'),
        ('博士', '博士'),
    )
    name = models.CharField(max_length=20, verbose_name='姓名')
    date_of_birth = models.CharField(max_length=20, verbose_name='出生年月')
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name='性别')
    education = models.CharField(max_length=5, choices=EDUCATION_CHOICES, verbose_name='学历')
    nation = models.CharField(max_length=10, verbose_name='民族')
    politics = models.CharField(max_length=10, verbose_name='政治面貌')
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    office_phone = models.CharField(max_length=10, verbose_name='办公电话')
    wechat = models.CharField(max_length=30, verbose_name='微信号')
    address = models.CharField(max_length=50, verbose_name='通信地址', default="")
    workplace = models.CharField(max_length=30, verbose_name='所在单位')
    duty = models.CharField(max_length=20, verbose_name='职务', blank=True, null=True)
    title = models.CharField(max_length=20, verbose_name='职称', blank=True, null=True)
    profession_field = models.TextField(max_length=200, verbose_name='专业领域')
    resume = models.TextField(max_length=500, verbose_name='曾获得荣誉', blank=True, null=True)

    class Meta:
        verbose_name = "会员申请信息"
