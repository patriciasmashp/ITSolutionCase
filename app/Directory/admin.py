from django.contrib import admin
from .models import Status, Subcategory, Category, Type
# Register your models here.
admin.site.register(Status)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Type)
