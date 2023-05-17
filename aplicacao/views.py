import os
import uuid

import qrcode
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from config.settings import BASE_DIR

from .models import Cardapio, Comanda, Mesa, Pedido
from .serializers import (CardapioSerializers, ComandaSerializers,
                          MesaSerializers, PedidoSerializers)

URL = 'www.url.com.br'


class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializers

    @action(methods=['get'], detail=False, url_path='buscar/(?P<nome>.+)')
    def buscar(self, request, nome=None):
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
    http_method_names = ['post', 'get', 'delete']

    @action(
        methods=['get'], detail=False, url_path='buscar/(?P<identificador>.+)'
    )
    def buscar(self, request, identificador=None):
        if identificador is not None:
            queryset = Mesa.objects.filter(
                identificador__icontains=identificador)
            serializer = MesaSerializers(queryset, many=True)

            if serializer.data == []:
                return Response({
                    "message": ("Não foi encontrado nenhuma"
                                "mesa com esse identificador")},
                                status=404
                                )

            return Response(serializer.data)
        else:
            return Response(
                {"message": "Não foi encontrado nenhuma mesa com esse nome"
                 },
                status=404
            )

    def create(self, request):
        try:
            identificador = uuid.uuid4()
            qrcode_mesa = qrcode.make(f'{URL}/mesa/{identificador}')
            qrcode_mesa.save(f'media/mesa/{identificador}.png')
            serializer = MesaSerializers(data={
                "identificador": str(identificador),
                "qrcode": f'{URL}/mesa/{identificador}',
                "caminho": f'{BASE_DIR}/media/mesa/{identificador}.png'
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    def destroy(self, request, pk=None):
        try:
            mesa = Mesa.objects.filter(pk=pk).first()

            if not mesa:
                return Response({"message": "Mesa não encontrada"},
                                status=404)

            mesa.delete()
            os.remove(mesa.caminho)

            return Response({"message": "Mesa deletada com sucesso"},
                            status=204)
        except Exception as e:
            return Response({"message": str(e)}, status=400)


class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializers
    http_method_names = ['post', 'get', 'delete', 'patch']

    @action(
        methods=['get'], detail=False, url_path='buscar/(?P<identificador>.+)'
    )
    def buscar(self, request, identificador=None):
        if identificador is not None:
            queryset = Comanda.objects.filter(
                identificador__icontains=identificador)
            serializer = ComandaSerializers(queryset, many=True)

            if serializer.data == []:
                return Response({
                    "message": ("Não foi encontrado nenhuma"
                                "comanda com esse identificador")},
                                status=404
                                )

            return Response(serializer.data)
        else:
            return Response(
                {"message": "Não foi encontrado nenhuma comanda com esse nome"
                 },
                status=404
            )

    def create(self, request):
        try:
            identificador = uuid.uuid4()
            qrcode_comanda = qrcode.make(
                f'{URL}/comanda/{identificador}')
            qrcode_comanda.save(f'media/comanda/{identificador}.png')
            serializer = ComandaSerializers(data={
                "identificador": str(identificador),
                "qrcode": f'{URL}/comanda/{identificador}',
                "caminho": f'{BASE_DIR}/media/comanda/{identificador}.png'
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    def destroy(self, request, pk=None):
        try:
            comanda = Comanda.objects.filter(pk=pk).first()

            if not comanda:
                return Response({"message": "Comanda não encontrada"},
                                status=404)

            comanda.delete()
            os.remove(comanda.caminho)

            return Response({"message": "Comanda deletada com sucesso"},
                            status=204)
        except Exception as e:
            return Response({"message": str(e)}, status=400)
