from django.urls import path, include
from rest_framework import routers
from .views import ConsultaClientesViewSet, ConsultaGaragensViewSet, consultaClientesGaragemVeiculosView, consultaClientesGaragemSVeiculosView

router = routers.DefaultRouter()

router.register('cons_clientes', ConsultaClientesViewSet)
router.register('cons_garagens', ConsultaGaragensViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cons_cli_garagem_veiculos/', consultaClientesGaragemVeiculosView),
    path('cons_cli_garagem_sveiculos/', consultaClientesGaragemSVeiculosView),
]
