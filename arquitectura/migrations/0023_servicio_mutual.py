# Generated by Django 2.2.19 on 2023-09-04 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consorcios', '0002_consorcio_costo_mp'),
        ('arquitectura', '0022_auto_20220510_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio_mutual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
                ('nombre_reglamento', models.CharField(blank=True, max_length=60, null=True)),
                ('fecha_reglamento', models.DateField(blank=True, null=True)),
                ('consorcio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consorcios.Consorcio')),
            ],
        ),
    ]
