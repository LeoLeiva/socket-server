# Generated by Django 3.2.16 on 2023-04-05 15:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('denomination', models.CharField(blank=True, choices=[('oficial', 'USD Oficial'), ('blue', 'USD Blue'), ('oficial_euro', 'Euro Oficial'), ('blue_euro', 'Euro Blue')], default='oficial', max_length=50, null=True)),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('price_buy', models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Precio de compra')),
                ('price_sell', models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Precio de venta')),
                ('description', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-id'],
            },
        ),
    ]
