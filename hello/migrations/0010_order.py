# Generated by Django 4.0.1 on 2022-03-24 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_rename_email_customer_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.customer')),
            ],
        ),
    ]
