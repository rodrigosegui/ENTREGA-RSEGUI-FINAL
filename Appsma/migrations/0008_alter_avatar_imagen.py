# Generated by Django 4.1.5 on 2023-02-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appsma', '0007_avatar_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='avatares'),
        ),
    ]
