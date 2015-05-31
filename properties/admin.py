from django.contrib import admin
from .models import Property

# Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'description']

admin.site.register(Property,PropertyAdmin)