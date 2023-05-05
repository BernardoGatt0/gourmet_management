from django.db import models


class Cardapio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False, blank=False)
    ingredientes = models.TextField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False, blank=False)
    caminho = models.TextField(max_length=100, null=100, blank=False)


class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    qrcode = models.TextField(null=False, blank=False)
    caminho = models.CharField(max_length=100, null=False, blank=False)
    total = models.FloatField(null=True, blank=False)


class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    qrcode = models.TextField(null=False, blank=False)
    caminho = models.CharField(max_length=100, null=False, blank=False)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    status = models.TextField(max_length=100, null=False, blank=False)




