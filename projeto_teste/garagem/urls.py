from django.urls import path, include
from rest_framework import routers
from .views import GaragemViewSet, VeiculoViewSet

router = routers.DefaultRouter()

router.register('garagem', GaragemViewSet)
router.register('veiculo', VeiculoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# Create your tests here.
