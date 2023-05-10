from rest_framework import viewsets
from .models import Cardapio, Comanda, Mesa, Pedido
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from drf_spectacular.openapi import OpenApiParameter

from .serializers import (CardapioSerializers, PedidoSerializers,
                          MesaSerializers, ComandaSerializers)


class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializers

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='nome',
                description='Nome do cardapio',
                required=True,
                type=str,
            )
        ],
    )
    @action(methods=['get'], detail=False)
    def buscar(self, request):
        nome = request.query_params.get('nome', None)
        if nome is not None:
            queryset = Cardapio.objects.filter(nome__icontains=nome)
            serializer = CardapioSerializers(queryset, many=True)

            if serializer.data == []:
                return Response({
                    "message": ("Não foi encontrado nenhum"
                                "cardapio com esse nome")}, status=404
                                )

            return Response(serializer.data)
        else:
            return Response(
                {"message": "Não foi encontrado nenhum cardapio com esse nome"
                 },
                status=404
            )


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializers


class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializers
