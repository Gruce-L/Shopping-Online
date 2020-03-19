# Generated by Django 2.1 on 2020-03-18 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0006_auto_20200317_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('proId', models.BigAutoField(primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=200)),
                ('proPrice', models.FloatField(default=0.0)),
                ('proImg', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userApp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userApp.UserInfo')),
            ],
        ),
    ]
