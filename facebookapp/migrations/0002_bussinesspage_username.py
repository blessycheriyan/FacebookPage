# Generated by Django 3.1.3 on 2020-11-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussinesspage',
            name='username',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]