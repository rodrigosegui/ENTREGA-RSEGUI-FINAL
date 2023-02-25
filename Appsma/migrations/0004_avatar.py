# Generated by Django 4.1.5 on 2023-02-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appsma', '0003_alter_clientes_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
            options={
                'verbose_name': 'Avatar',
                'verbose_name_plural': 'Avatares',
            },
        ),
    ]