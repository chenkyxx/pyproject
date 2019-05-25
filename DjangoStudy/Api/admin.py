from django.contrib import admin
from Api.models import IMG

# Register your models here.


class ImgDemo(admin.ModelAdmin):
    list_display = ["name", "img"]
