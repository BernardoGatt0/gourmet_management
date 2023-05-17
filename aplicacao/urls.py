from django.urls import path, include
from rest_framework import routers
from .views import CardapioViewSet, MesaViewSet, ComandaViewSet, PedidoViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cardapio', CardapioViewSet)
router.register(r'mesa', MesaViewSet)
router.register(r'comanda', ComandaViewSet)
router.register(r'pedido', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
