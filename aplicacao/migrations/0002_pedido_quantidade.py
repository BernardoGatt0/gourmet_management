# Generated by Django 4.2 on 2023-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
