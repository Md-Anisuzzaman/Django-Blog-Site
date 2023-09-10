# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Account


# class AccountAdmin(UserAdmin):
#     list_display = ('id','email', 'username', 'role', 'date_joined',
#                     'last_login', 'phone_number')
#     list_display_links = ('email',)
#     readonly_fields = ('date_joined', 'last_login')
#     ordering = ('-date_joined',)
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


# admin.site.register(Account, AccountAdmin)

from .models import RegistrationModel
from django.contrib import admin

admin.site.register(RegistrationModel)
admin.site.register(RegistrationModel)