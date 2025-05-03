from django.urls import path
from .views import DepartmentAPIView
from .views import BatchAPIView
from .views import DepartmentModifyView
from .views import BatchModifyView

urlpatterns = [
    path("deparments_view/", DepartmentAPIView.as_view()),
    path("batchs_view/", BatchAPIView.as_view()),
    path("deparments_modify_view/<int:id>/", DepartmentModifyView.as_view()),
    path("batchs_modify_view/<int:id>/", BatchModifyView.as_view()),
]
