from django.contrib import admin

# Register your models here.
from .models import People, Daycare

admin.site.register(People)
admin.site.register(Daycare)
