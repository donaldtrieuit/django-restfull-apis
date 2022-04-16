from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import StoreApiView

router = DefaultRouter()
router.register(r'stores', StoreApiView, basename='stores')

urlpatterns = [
    path('', include(router.urls)),
]