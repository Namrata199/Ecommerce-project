# Generated by Django 3.1.2 on 2020-12-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_module', '0003_invoice_invoicedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentgateway',
            name='token',
            field=models.UUIDField(unique=True),
        ),
    ]
