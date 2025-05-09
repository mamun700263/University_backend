from django.urls import path

from .views import UniversityAPIView, UniversityModifyView

urlpatterns = [
    path
    (
        "universiy_api/",
        UniversityAPIView.as_view(),
        name="university"
    ),
    path
    (
        "universiy_modify_api/<int:id>/",
        UniversityModifyView.as_view(),
        name="university_modify_api",
    ),
]
