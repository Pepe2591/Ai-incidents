from django.contrib import admin
from .models import Camera, Dangerous_event, Category

# Register your models here.

admin.site.register(Camera)
admin.site.register(Dangerous_event)
admin.site.register(Category)
