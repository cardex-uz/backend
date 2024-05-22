from core.routers import DefaultRouter
from api.management.urls import router as management_router
from api.order.urls import router as orders_router
from api.product.urls import router as products_router

router = DefaultRouter()
router.extend(management_router)
router.extend(orders_router)
router.extend(products_router)
