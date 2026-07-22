from rest_framework.routers import DefaultRouter
from events.views import ExplosionModelViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('explosions', ExplosionModelViewSet, 'explosion')

urlpatterns = [
    path('', include(router.urls))
]