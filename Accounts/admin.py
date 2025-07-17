from django.contrib import admin


from .models import (
    UniUser,
    AuthorityAccount,
    StaffAccount,
    StudentAccount,
    TeacherAccount
    )


admin.site.register(StudentAccount)
admin.site.register(TeacherAccount)
admin.site.register(AuthorityAccount)
admin.site.register(StaffAccount)
