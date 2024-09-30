from django.contrib import admin
from .models import category,product

# Register your models here.


class showcategory(admin.ModelAdmin):
    list_display = ["name","description"]


admin.site.register(category,showcategory)

class showproduct(admin.ModelAdmin):
    list_display = ["name","price","description","quantity","catid"]

admin.site.register(product,showproduct)