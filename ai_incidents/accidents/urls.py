from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CameraModelViewSet, FiresModelViewSet, ExplosionModelViewSet, 
                    CollapseMidelViewSet, CoreSericeViewSet, LogsViewSet, AnalysisViewSet)

router = DefaultRouter()
router.register(r'cameras', CameraModelViewSet, basename='camera') 



urlpatterns = [
    path('', include(router.urls))
]   