from django.contrib import admin
from .models import Department
from .models import Batch
# Register your models here.
# make sure to add the app in the installed app list
admin.site.register(Department)
admin.site.register(Batch)