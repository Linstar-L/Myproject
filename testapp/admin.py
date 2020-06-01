from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mezzanine.accounts.admin import User

from copy import deepcopy

# admin.site.register(User, MyUserAdmin)
from mezzanine.utils.admin import SingletonAdmin
#from .models import SiteAlert


# Subclassing allows us to customize the admin class,
# but you could also register your model directly
# against SingletonAdmin below.
#class SiteAlertAdmin(SingletonAdmin):
    #pass


#admin.site.register(SiteAlert, SiteAlertAdmin)
