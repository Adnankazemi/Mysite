
from django.contrib import admin
from django.urls import path
from shop.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('', home),
    path('login/', login),
    path('contact/', contact_us),
]
handler404 = 'shop.views.custom_404'