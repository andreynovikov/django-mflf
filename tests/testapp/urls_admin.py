from django.contrib import admin
from django.urls import path

from testapp.models import Product


admin_site = admin.AdminSite()
admin_site.register(Product)

urlpatterns = [
    path('admin/', admin_site.urls),
]
