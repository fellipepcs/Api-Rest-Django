# Generated by Django 3.2.9 on 2021-11-15 14:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('idbook', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('data', models.DateTimeField(auto_now=True)),
                ('estadoLivro', models.CharField(max_length=50)),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=255)),
                ('dataDeCriação', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
