from django.contrib import admin


from .models import (
    Account,
    AuthorityAccount,
    StaffAccount,
    StudentAccount,
    TeacherAccount
    )


# Register your models here.
# make sure to add the app in the installed app list
# admin.site.register(Account)
admin.site.register(StudentAccount)
admin.site.register(TeacherAccount)
admin.site.register(AuthorityAccount)
admin.site.register(StaffAccount)
