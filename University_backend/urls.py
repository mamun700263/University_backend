from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔗 API Route Groups
    path('api/', include([
        path('accounts/', include('Accounts.urls')),        # /api/accounts/
        path('universities/', include('university.urls')),  # /api/universities/
        path('departments/', include('Departments.urls')),  # /api/departments/
        path('batches/', include('batch.urls')),            # /api/batches/
        # 👇 Add more modules here as needed
    ])),

    # 📄 API Schema + Swagger Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
