from django.contrib import admin

# Register your models here.
from app1.models import MeetingApp


class meetingadmin(admin.ModelAdmin):
    list_display = ['name', 'workplace', 'mobile', 'email', 'sign']
    list_filter = ['name']


admin.site.register(MeetingApp, meetingadmin)
