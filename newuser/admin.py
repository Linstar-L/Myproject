from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from newuser.models import NewUser

# Register your models here.
from testapp.models import MyProfile


class ProfileInline(admin.StackedInline):
    model = MyProfile
    # can_delete = False
    verbose_name = '会员信息'
    verbose_name_plural = '会员信息'


class NewUserAdmin(UserAdmin):
    inlines = (ProfileInline,)  # 将MyProfile的数据植入后台用户信息
    list_display = ['username', 'email', 'is_active']
    # list_filter = ['name']
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
                 ('Important dates', {'fields': ('last_login', 'date_joined')}))

    def activate_user(ModelAdmin, request, queryset):  # 编写后台激活用户功能
        queryset.update(is_active=True)

    activate_user.short_description = "激活用户"
    actions = [activate_user]


admin.site.unregister(NewUser)
admin.site.unregister(Group)  # 移除后台管理的群组功能管理界面
admin.site.register(NewUser, NewUserAdmin)
