from django.db import models


class Cardapio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False, blank=False)
    ingredientes = models.TextField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False, blank=False)
    caminho = models.TextField(max_length=100, null=100, blank=False)

    def __str__(self):
        return self.nome


class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    qrcode = models.TextField(null=False, blank=False)
    caminho = models.CharField(max_length=100, null=False, blank=False)
    total = models.FloatField(null=True, blank=False, default=0.0)
    identificador = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.id)


class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    qrcode = models.TextField(null=False, blank=False)
    caminho = models.CharField(max_length=100, null=False, blank=False)
    identificador = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.id)


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    status = models.TextField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return str(self.id)
