# Generated by Django 3.0.2 on 2020-05-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_token',
            field=models.CharField(max_length=50, verbose_name='verification token'),
        ),
    ]
