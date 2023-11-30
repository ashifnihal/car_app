from django.db import models

# Create your models here.
class CarModels(models.Model):
    sno = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100, default=None)
    year = models.IntegerField()
    image = models.CharField(max_length=500)
    new_or_pre_owned = models.CharField(max_length=100, choices=[('new', 'New'), ('pre_owned', 'Pre_Owned')])

class CarOverview(CarModels):
    varient_choices = [('diesel', 'Diesel'), ('petrol')]
    varients = models.CharField(max_length=1000)
    ex_showroom_price = models.FloatField()
    milage = models.CharField(max_length=1000)
    engine = models.CharField(max_length=1000)
    transmission = models.CharField(max_length=1000)
    kilometer_reading = models.FloatField()
    seating_capacity = models.IntegerField()
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('white', 'White')
        # Add more colors as needed
    ]
    colors = models.CharField(max_length=20, choices=COLOR_CHOICES)
    user_review = models.FloatField()
    description = models.TextField()


class CustomManager(models.Manager):

    def get_carbrands_sorted_by(self, param):
        return super().get_queryset().order_by(param)

class CarBrands(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    objects = CustomManager()



