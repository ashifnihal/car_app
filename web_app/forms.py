import re
from django import forms
from .models import CarBrands, CarOverview, PreOwnedCarsOverview, UpcomingCarOverview, CarUser

class AddPreOwnedCarOverviewForm(forms.ModelForm):
    class Meta:
        model = PreOwnedCarsOverview
        fields = "__all__"

    def clean(self):
        year = self.cleaned_data['year']
        type = self.cleaned_data['type']
        bname = self.cleaned_data['bname']
        model = self.cleaned_data['model']
        if not year or not type or not bname or not model:
            raise forms.ValidationError("Please fill all the fields")
        types = ["SUV", "MPV", "SEDAN", "HATCHBACK", "COMPACT SUV", "WAGON"]
        if year > 2023:
            raise forms.ValidationError("year shoud not be more than current year")
        if type.upper() not in types:
            raise forms.ValidationError(f"type should be one of these {types}")

class AddCarForm(forms.Form):

    bname = forms.CharField()
    type = forms.CharField()
    model = forms.CharField()
    year = forms.IntegerField()
    boat_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):

        year = self.cleaned_data['year']
        type = self.cleaned_data['type']
        bname = self.cleaned_data['bname']
        model =self.cleaned_data['model']
        if not year or not type or not bname or not model:
            raise forms.ValidationError("Please fill all the fields")
        types = ["SUV", "MPV", "SEDAN", "HATCHBACK", "COMPACT SUV", "WAGON"]

        if year>2023:
            raise forms.ValidationError("year shoud not be more than current year")
        boat_handler = self.cleaned_data['boat_handler']
        if len(boat_handler)>0:
            raise forms.ValidationError(f"request from bot cannot be submitted")
        if type.upper() not in types:
            raise forms.ValidationError(f"type should be one of these {types}")

class AddCarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrands
        fields = "__all__"

class AddCarOverviewForm(forms.ModelForm):
    class Meta:
        model = CarOverview
        fields = "__all__"

    def clean(self):
        year = self.cleaned_data['year']
        type = self.cleaned_data['type']
        bname = self.cleaned_data['bname']
        model = self.cleaned_data['model']
        if not year or not type or not bname or not model:
            raise forms.ValidationError("Please fill all the fields")
        types = ["SUV", "MPV", "SEDAN", "HATCHBACK", "COMPACT SUV", "WAGON"]
        if year > 2023:
            raise forms.ValidationError("year shoud not be more than current year")
        if type.upper() not in types:
            raise forms.ValidationError(f"type should be one of these {types}")

class AddUpcomingCarOverviewForm(forms.ModelForm):

    class Meta:
        model = UpcomingCarOverview
        fields = "__all__"

    def clean(self):
        year = self.cleaned_data['year']
        type = self.cleaned_data['type']
        bname = self.cleaned_data['bname']
        model = self.cleaned_data['model']
        if not year or not type or not bname or not model:
            raise forms.ValidationError("Please fill all the fields")
        types = ["SUV", "MPV", "SEDAN", "HATCHBACK", "COMPACT SUV", "WAGON"]
        # if year > 2023:
        #     raise forms.ValidationError("year shoud not be more than current year")
        if type.upper() not in types:
            raise forms.ValidationError(f"type should be one of these {types}")

class RegisterUserForm(forms.ModelForm):

    class Meta:
        model = CarUser
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean(self):
        password = self.cleaned_data['password']
        mobile_no = self.cleaned_data["mobile_no"]
        email = self.cleaned_data["email"]
        if len(password)<8 or len(password)>12:
            raise forms.ValidationError(f"password contains min 8 chars and max 12 chars")
        if (not re.search(r'[A-Z]', password) or
                not re.search(r'[a-z]', password) or
                not re.search(r'[0-9]', password) or
                not re.search(r"[ !@#$%^&*()_+=\[{\]};:<>|./?,-]", password)):
            raise forms.ValidationError('password must contains at least 1 capital letter and 1 '
                                        'small letter and 1 digit [0-9] and 1 special character !@#$%^&*()_+=\[{\]};:<>|./?')
        if len(str(mobile_no))<10 or len(str(mobile_no))>12:
            raise forms.ValidationError("please enter a valid mobile no")
        try:
            car_data = CarUser.objects.get(email=email)
            if car_data:
                raise forms.ValidationError("User already registered")
        except CarUser.DoesNotExist:
            print("valid case")

