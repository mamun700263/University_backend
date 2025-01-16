from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import (
    AccountViewSet,
    StudentAccountViewSet,
    TeacherAccountViewSet,
    StaffAccountViewSet,
    AuthorityAccountViewSet,
)

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'students', StudentAccountViewSet)
router.register(r'teachers', TeacherAccountViewSet)
router.register(r'staffs', StaffAccountViewSet)
router.register(r'authorities', AuthorityAccountViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)), 
    
]