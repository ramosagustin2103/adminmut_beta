# Generated by Django 2.2.19 on 2023-09-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0025_auto_20230904_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_mutual',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]