# Generated by Django 4.0.5 on 2022-06-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=40)),
                ('nro_vuelo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('notas', models.CharField(max_length=200)),
            ],
        ),
    ]