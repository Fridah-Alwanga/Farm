from django.contrib import admin
from .models import Admin,Farmers,Suppliers


# Register your models here.
admin.site.register(Admin)
admin.site.register(Farmers)
admin.site.register(Suppliers)
