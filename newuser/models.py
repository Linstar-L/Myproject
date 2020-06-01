from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from testapp.models import MyProfile


class NewUser(AbstractUser):
    pass
    class Meta:
        verbose_name_plural = '会员申请'
    # def save(self, commit=True):
    #     instance = super().save(commit=True)  # 继承的类（UserCreationForm)保存的对象实例
    #     profile = MyProfile(user=instance, name=self.cleaned_data["name"],
    #                         gender=self.cleaned_data["gender"],
    #                         workplace=self.cleaned_data["workplace"], mobile=self.cleaned_data["moblile"],
    #                         duty=self.cleaned_data["duty"], title=self.cleaned_data["title"],
    #                         resume=self.cleaned_data["resume"])
    #     profile.save()
    #     return profile
