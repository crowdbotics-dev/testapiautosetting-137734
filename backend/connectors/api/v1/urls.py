from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137734ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137734", Testconnectors137734ViewSet, basename="testconnectors137734"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
