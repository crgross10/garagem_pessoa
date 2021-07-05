from django.urls import path, include
from .views import PessoaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
