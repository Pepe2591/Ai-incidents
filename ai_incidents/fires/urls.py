from rest_framework.routers import DefaultRouter
from events.views import FiresModelViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('fires', FiresModelViewSet, 'fire')

urlpatterns = [
    path('', include(router.urls))
]