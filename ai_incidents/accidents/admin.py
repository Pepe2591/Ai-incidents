from django.contrib import admin
from .models import Camera, Event, Category

# Register your models here.

admin.site.register(Camera)
admin.site.register(Event)
admin.site.register(Category)
