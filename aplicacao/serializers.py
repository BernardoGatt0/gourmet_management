from rest_framework import serializers
from .models import Cardapio, Mesa, Comanda, Pedido


class CardapioSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cardapio
        fields = '__all__'


class MesaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'


class ComandaSerializers(serializers.ModelSerializer):
    total = serializers.FloatField(default=0.0)

    class Meta:
        model = Comanda
        fields = '__all__'


class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
