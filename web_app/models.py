from django.db import models

# Create your models here.
class CarModels(models.Model):
    sno = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100, default=None)
    year = models.IntegerField()
    image = models.CharField(max_length=500)
    new_or_pre_owned_or_upcoming = models.CharField(max_length=100, choices=[('new', 'New'), ('pre_owned', 'Pre_Owned'), ('up_coming', 'Up_Coming')])

class CarOverview(CarModels):
    varients = models.CharField(max_length=1000)
    ex_showroom_price = models.FloatField()
    milage = models.CharField(max_length=1000)
    engine = models.CharField(max_length=1000)
    transmission = models.CharField(max_length=1000)
    seating_capacity = models.IntegerField()
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('white', 'White'),
        ('other', 'Other')
        # Add more colors as needed
    ]
    colors = models.CharField(max_length=20, choices=COLOR_CHOICES)
    user_review = models.FloatField()
    description = models.TextField()

class PreOwnedCarsOverview(CarModels):
    varient_choices = [('diesel', 'Diesel'), ('petrol', 'Petrol'), ('cng', 'Cng'), ('ev', 'Ev')]
    no_of_owners = models.IntegerField()
    images = models.ImageField(upload_to='static/images/pre_owned_cars/')
    price = models.FloatField()
    drive_train = models.CharField(max_length=1000, choices=[('awd', 'AWD'),('rwd', 'RWD')])
    fuel_type = models.CharField(max_length=1000, choices=varient_choices)
    engine = models.CharField(max_length=1000)
    kilometer_reading = models.FloatField()
    registration_year = models.IntegerField()
    transmission = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    pin_code = models.IntegerField()
    address = models.TextField()
    headline = models.CharField(max_length=5000)

class UpcomingCarOverview(CarOverview):
    expected_release_date = models.DateField()
    images = models.ImageField(upload_to='static/images/upcoming_cars/')
    expected_price_range = models.CharField(max_length=1000)



class CustomManager(models.Manager):

    def get_carbrands_sorted_by(self, param):
        return super().get_queryset().order_by(param)

class CarBrands(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    objects = CustomManager()

class CarUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    mobile_no = models.IntegerField()
    is_loggedin = models.BooleanField(default=False)




