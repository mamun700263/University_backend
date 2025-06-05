

from django.contrib import admin
from django.urls import include, path

from Accounts import urls as account_url
from Departments import urls as deparment_url
from university import urls as university_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include(account_url)),
    path("departments/", include(deparment_url)),
    path("university/", include(university_url)),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Unified API entrypoint
    path('api/', include([
        path('', include('university.urls')),   # /api/universities/
        path('', include('Accounts.urls')),     # /api/students/
        path('', include('Departments.urls')),      # /api/courses/
        path('', include('batch.urls')),    #/api/batch
        # add more as needed
    ])),
]
