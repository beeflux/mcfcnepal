from django.contrib import admin

# Register your models here.
from .models import Members, AdminMember

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','position','contact_no')
admin.site.register(Members)
admin.site.register(AdminMember, MemberAdmin)