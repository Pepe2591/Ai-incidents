from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CameraModelViewSet, FiresModelViewSet, ExplosionModelViewSet, 
                    CollapseMidelViewSet, CoreSericeViewSet, LogsViewSet, AnalysisViewSet)

router = DefaultRouter()
router.register(r'cameras', CameraModelViewSet, basename='camera')
router.register(r'fires', FiresModelViewSet, basename='fire')
router.register(r'explosions', ExplosionModelViewSet, basename='explosion')
router.register(r'collapse', CollapseMidelViewSet, basename='collapse')
router.register(r'core-service', CoreSericeViewSet, basename='core-service')
router.register(r'logs', LogsViewSet, basename='log')
router.register(r'analysis', AnalysisViewSet, basename='analysis')


urlpatterns = [
    path('', include(router.urls))
]   