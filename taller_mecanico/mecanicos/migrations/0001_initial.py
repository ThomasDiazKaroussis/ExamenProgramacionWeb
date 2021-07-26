# Generated by Django 3.2.4 on 2021-06-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mecanico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='publicaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_trabajo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
