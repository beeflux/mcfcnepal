from django.contrib import admin
from simple_history import register

# Register your models here.
from .models import Events
admin.site.register(Events)

