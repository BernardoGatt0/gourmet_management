from django.urls import path, include
from rest_framework import routers
from .views import CardapioViewSet, MesaViewSet, ComandaViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'Cardapio', CardapioViewSet)
router.register(r'Mesa', MesaViewSet)
router.register(r'Comanda', ComandaViewSet)
router.register(r'Pedido', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls))
]