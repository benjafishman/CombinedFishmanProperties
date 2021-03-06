from django.contrib import admin
from .models import Apartment, Property

# Register your models here.

'''
class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 3
'''

class PropertyAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'description', 'history', 'image_file', 'number_of_layouts']
    #inlines = [ApartmentInline]

admin.site.register(Property,PropertyAdmin)