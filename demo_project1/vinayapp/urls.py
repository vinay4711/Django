from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.custViewSet, base_name='custViewSet')
urlpatterns = router.urls