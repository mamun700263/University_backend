from django.urls import path
from .views import UniversityViewSet
urlpatterns = [
    path('universiy/', UniversityViewSet.as_view(), name='university'),
]
