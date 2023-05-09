from django.contrib import admin

from aplicacao import models


@admin.register(models.Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'nome', 'ingredientes', 'valor',
                    'descricao', 'status', 'caminho')


@admin.register(models.Comanda)
class ComandaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'qrcode', 'caminho', 'total')


@admin.register(models.Mesa)
class MesaAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'qrcode', 'caminho')


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'cardapio', 'comanda', 'mesa', 'status')
