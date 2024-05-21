from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CustomerViewSet, ProviderViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'devices', DeviceViewSet)
