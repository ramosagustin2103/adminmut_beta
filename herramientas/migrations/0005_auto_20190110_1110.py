# Generated by Django 2.0.3 on 2019-01-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0004_auto_20190110_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='transferencias/pdf/'),
        ),
    ]
