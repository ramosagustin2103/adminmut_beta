# Generated by Django 2.2.19 on 2022-05-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0013_socio_notificaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='numero_asociado',
            field=models.PositiveIntegerField(default=1),
        ),
    ]