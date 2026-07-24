from rest_framework.routers import DefaultRouter
from events.views import CollapseModelViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('collapses', CollapseModelViewSet, 'collapse')

urlpatterns = [
    path('', include(router.urls))
]