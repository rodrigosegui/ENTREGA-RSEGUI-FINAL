# Generated by Django 4.1.5 on 2023-02-24 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appsma', '0005_alter_avatar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avatar',
            options={'verbose_name': 'Avatar', 'verbose_name_plural': 'Avatares'},
        ),
    ]