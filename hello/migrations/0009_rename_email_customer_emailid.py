# Generated by Django 4.0.1 on 2022-03-24 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_rename_emailid_customer_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='emailid',
        ),
    ]
