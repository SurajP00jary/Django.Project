# Generated by Django 4.0.1 on 2022-03-24 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_alter_order_product_id_alter_order_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='productname',
        ),
    ]
