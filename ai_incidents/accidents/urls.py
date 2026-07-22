from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import 

router = DefaultRouter()
router.register(r'cameras', CameraModelViewSet, basename='camera') 


urlpatterns = [
    path('', include(router.urls))
]