from rest_framework import serializers
from .models import Cardapio, Mesa, Comanda, Pedido

class CardapioSerializers(serializers.Serializer):
    class Meta:
        model = Cardapio
        fields = '__all__'

class MesaSerializers(serializers.Serializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class ComandaSerializers(serializers.Serializer):
    class Meta:
        model = Comanda
        fields = '__all__'

class PedidoSerializers(serializers.Serializer):
    class Meta:
        model = Pedido
        fields = '__all__'