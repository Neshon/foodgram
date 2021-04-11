from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import FavoriteViewSet, FollowViewSet, PurchaseViewSet, IngredientViewSet

router = DefaultRouter()
router.register('favorites', FavoriteViewSet)
router.register('subscriptions', FollowViewSet)
router.register('purchases', PurchaseViewSet)
router.register('ingredients', IngredientViewSet)


urlpatterns = [
    path('v1/', include(router.urls))
]
