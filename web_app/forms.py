from django import forms
from .models import CarBrands, CarOverview
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
