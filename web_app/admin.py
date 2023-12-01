from django.contrib import admin
from .models import CarModels, CarBrands, CarOverview, PreOwnedCarsOverview
# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["bname", "type", "model", "year", "image", "new_or_pre_owned"]
class CarBrandsAdmin(admin.ModelAdmin):
    list_display = ["sno", "name", "country"]
class CarOverviewAdmin(admin.ModelAdmin):
    model_fields = [field.name for field in CarOverview._meta.get_fields()]
    list_display = model_fields
class PreOwnedCarOverviewAdmin(admin.ModelAdmin):
    model_fields = [field.name for field in PreOwnedCarsOverview._meta.get_fields()]
    list_display = model_fields

admin.site.register(CarModels, CarModelAdmin)
admin.site.register(CarBrands, CarBrandsAdmin)
admin.site.register(CarOverview, CarOverviewAdmin)
admin.site.register(PreOwnedCarsOverview, PreOwnedCarOverviewAdmin)
# admin.site.register(all_models)
