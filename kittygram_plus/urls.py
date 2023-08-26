from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'mycats', LightCatViewSet)
router.register(r'owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
