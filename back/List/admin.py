from django.contrib import admin
from .models import Food
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Ingredients')

# Register your models here.

admin.site.register(Food, FoodAdmin)
