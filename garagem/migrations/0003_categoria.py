# Generated by Django 4.1.7 on 2023-03-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_marca_delete_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
