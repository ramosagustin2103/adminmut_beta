# Generated by Django 2.2.19 on 2022-05-10 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0020_auto_20220510_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socio',
            name='cuenta_contable',
        ),
    ]