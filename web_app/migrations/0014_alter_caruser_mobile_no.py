# Generated by Django 3.2.23 on 2023-12-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0013_caruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caruser',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]