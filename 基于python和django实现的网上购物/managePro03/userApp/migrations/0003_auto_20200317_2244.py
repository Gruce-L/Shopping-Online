# Generated by Django 2.1 on 2020-03-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20200317_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='userBirth',
            field=models.DateField(null=True),
        ),
    ]
