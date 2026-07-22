from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import AccidentModelViewSet

router = DefaultRouter()
router.register(r'accidents', AccidentModelViewSet, basename='accident') 


urlpatterns = [
    path('', include(router.urls))
]