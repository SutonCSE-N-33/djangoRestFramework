from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductReviewViewSet


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'review', ProductReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
]