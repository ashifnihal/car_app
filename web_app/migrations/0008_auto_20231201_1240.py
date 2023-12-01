# Generated by Django 3.1.4 on 2023-12-01 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_caroverview_kilometer_reading'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreOwnedCarsOverview',
            fields=[
                ('carmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web_app.carmodels')),
                ('no_of_owners', models.IntegerField()),
                ('price', models.FloatField()),
                ('drive_train', models.CharField(choices=[('awd', 'AWD'), ('rwd', 'RWD')], max_length=1000)),
                ('fuel_type', models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('cng', 'Cng'), ('ev', 'Ev')], max_length=1000)),
                ('engine', models.CharField(max_length=1000)),
                ('kilometer_reading', models.FloatField()),
                ('registration_year', models.IntegerField()),
                ('transmission', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('pin_code', models.IntegerField()),
                ('address', models.TextField()),
                ('headline', models.CharField(max_length=5000)),
            ],
            bases=('web_app.carmodels',),
        ),
        migrations.RemoveField(
            model_name='caroverview',
            name='kilometer_reading',
        ),
        migrations.AlterField(
            model_name='caroverview',
            name='colors',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('white', 'White'), ('other', 'Other')], max_length=20),
        ),
    ]
