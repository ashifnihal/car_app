# Generated by Django 3.2.23 on 2023-12-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_auto_20231201_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='preownedcarsoverview',
            name='images',
            field=models.ImageField(default='NA', upload_to='..static/images/pre_owned_cars/'),
            preserve_default=False,
        ),
    ]