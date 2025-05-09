from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AccountViewSet,
    AuthorityAccountViewSet,
    StaffAccountViewSet,
    StudentAccountViewSet,
    TeacherAccountViewSet,
    UserLoginApiView
    )

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"students", StudentAccountViewSet)
router.register(r"teachers", TeacherAccountViewSet)
router.register(r"staffs", StaffAccountViewSet)
router.register(r"authorities", AuthorityAccountViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    path("login/", UserLoginApiView.as_view(), name="login"),
]
