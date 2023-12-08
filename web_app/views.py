from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import CarModels, CarBrands, CarOverview, PreOwnedCarsOverview, UpcomingCarOverview, CarUser
from . import forms

# Create your views here.


def get_details(request):
    return HttpResponse("<h1>Welcome to django web app</h1>")

def get_cars(request):
    car_data = CarModels.objects.all()
    return render(request, "web_app/car_home.html", {"car_data":car_data.values()})

def get_carbrands(request):
    brands = CarBrands.objects.get_carbrands_sorted_by('sno')
    return render(request, "web_app/brands.html", {"car_brands": brands.values})

def get_carmodels(request):
    models = ["Q7", "A4", "X5", "Superb", "Kushaq",
              "rapid", "octavia", "polo", "vento",
              "jetta", "seltos", "sonet", "carens",
              "nexon", "safari", "harrier"]
    return render(request, "web_app/models.html", {"car_models": models})

def get_cartypes(request):
    types = ["SUV", "MUV", "SEDEN", "HATCHBACK", "COMPACT SUV", "WAGON"]
    return render(request, "web_app/types.html", {"car_types": types})

def carInputView(request):
    form = forms.AddCarForm()
    if request.method == 'POST':
        form = forms.AddCarForm(request.POST)
        if form.is_valid():
            print("form validation success")
            print(f"bname: {form.cleaned_data['bname']}")
            print(f"type: {form.cleaned_data['type']}")
            print(f"model: {form.cleaned_data['model']}")
            print(f"year: {form.cleaned_data['year']}")
            CarModels.objects.create(bname=form.cleaned_data['bname'],
                                      type=form.cleaned_data['type'],
                                      model=form.cleaned_data['model'].replace(' ', ''),
                                      year=form.cleaned_data['year'])
            return HttpResponse(content="Form filled successfully")
    add_car = {"add_car": form}
    return render(request, "web_app/car_input.html", context=add_car)


def add_car_brands(request):
    add_brands_form = forms.AddCarBrandForm
    if request.method == "POST":
        add_brands_form = forms.AddCarBrandForm(request.POST)
        if add_brands_form.is_valid():
            name = add_brands_form.cleaned_data['name']
            country = add_brands_form.cleaned_data['country']
            print(f"name:{name} country:{country}")
            add_brands_form.save(commit=True)
    add_car_brands = {"add_car_brands":add_brands_form}
    return render(request, "web_app/brands_input.html", context=add_car_brands)

def show_new_cars(request):
    return render(request, "web_app/new_cars.html")

def show_pre_owned_cars(request):
    return render(request, "web_app/pre-owned-car-brands.html")

def show_upcomming_cars(request):
    return render(request, "web_app/upcomming_car_brands.html")

def get_cars_by_brand(request, bname, new_or_pre_owned):
    print(f"bname:{bname}")
    if new_or_pre_owned.lower() in ["new", 'upcoming']:
        all_cars = CarModels.objects.filter(bname=bname, new_or_pre_owned_or_upcoming=new_or_pre_owned)
    else:
        all_cars = [CarModels.objects.filter(bname=bname, new_or_pre_owned_or_upcoming=new_or_pre_owned).first()]
    print(f"all cars : {all_cars}")
    car_list = {"car_list":all_cars}
    return render(request, "web_app/all_cars.html", context=car_list)

# def add_car_overview(request):
#     add_car_overview_form = forms.AddCarOverviewForm
#     if request.method == 'POST':
#         add_car_overview_form = forms.AddCarOverviewForm(request.POST)
#         if add_car_overview_form.is_valid():
#             bname = add_car_overview_form.cleaned_data['bname']
#             print(f"bname: {bname}")
#             add_car_overview_form.save(commit=True)
#     add_car_overview = {"add_car_overview":add_car_overview_form}
#     return render(request, "web_app/car_overview_input.html", context=add_car_overview)

def add_car_overview(request):
    if request.method == 'POST':
        add_car_overview_form = forms.AddCarOverviewForm(request.POST)
        if add_car_overview_form.is_valid():
            # Create an instance of the form
            new_car_overview = add_car_overview_form.save(commit=False)  # Commit=False to prevent saving to the database immediately

            # Access and handle form data
            bname = add_car_overview_form.cleaned_data['bname']
            print(f"bname: {bname}")

            # Perform additional operations on new_car_overview if needed
            # new_car_overview.some_field = some_value

            # Save the instance to the database
            new_car_overview.save()

            # Redirect or perform any other action after saving
            add_car_overview_form = forms.AddCarOverviewForm()

    else:
        add_car_overview_form = forms.AddCarOverviewForm()

    add_car_overview = {"add_car_overview": add_car_overview_form}
    return render(request, "web_app/car_overview_input.html", context=add_car_overview)

def add_preowned_car_overview(request):
    if request.method == 'POST':
        add_pre_owned_car_form = forms.AddPreOwnedCarOverviewForm(request.POST, request.FILES)
        if add_pre_owned_car_form.is_valid():
            add_pre_owned_car_form.save()
            add_pre_owned_car_form = forms.AddPreOwnedCarOverviewForm()
    else:
        add_pre_owned_car_form = forms.AddPreOwnedCarOverviewForm()
    return render(request, "web_app/pre_owned_car_input.html", context={"add_pre_owned_car": add_pre_owned_car_form})

def add_upcoming_car_overview(request):
    if request.method == 'POST':
        add_upcoming_car_form = forms.AddUpcomingCarOverviewForm(request.POST, request.FILES)
        if add_upcoming_car_form.is_valid():
            add_upcoming_car_form.save()
            add_upcoming_car_form = forms.AddUpcomingCarOverviewForm()
    else:
        add_upcoming_car_form = forms.AddUpcomingCarOverviewForm()
    return render(request, "web_app/add_upcoming_car_input.html", context={"add_upcoming_car": add_upcoming_car_form})

def get_preowned_car_overview(request, car_model):
    get_car_overview = PreOwnedCarsOverview.objects.filter(model=car_model)
    car_overview = {"car_overview": get_car_overview}
    return render(request, "web_app/pre_owned_car_overview.html", context=car_overview)

def get_upcoming_car_overview(request, car_model):
    get_car_overview = UpcomingCarOverview.objects.filter(model=car_model)
    car_overview = {"car_overview": get_car_overview}
    return render(request, "web_app/upcoming_car_overview.html", context=car_overview)

def register_user(request):
    if request.method == 'POST':
        register_user_form = forms.RegisterUserForm(request.POST)
        if register_user_form.is_valid():
            register_user_form.save()
            return render(request, "web_app/new_cars.html")
    else:
        register_user_form = forms.RegisterUserForm()
    return render(request, "web_app/register_user.html", context = {"register_user": register_user_form})

def user_login(request):
    user_login_form = forms.UserLoginForm()
    if request.method == 'POST':
        user_login_form = forms.UserLoginForm(request.POST)

        if user_login_form.is_valid():
            return render(request, "web_app/car_home.html")
    return render(request, "web_app/login.html", context={"login_user": user_login_form})


class CarOverviewView(View):

    def get(self, request, car_model, *args, **kwargs):
        get_car_overview = CarOverview.objects.filter(model=car_model, new_or_pre_owned_or_upcoming='new')
        print(f"car overview:{get_car_overview}")
        car_overview = {"car_overview":get_car_overview}
        return render(request, "web_app/car_overview.html", context=car_overview)



