from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, TypeViewSet, TemplateViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('Types', TypeViewSet)
router.register('templates', TemplateViewSet)
router.register('products', ProductViewSet)
