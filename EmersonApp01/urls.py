from django.contrib import admin
from django.urls import path
from EmersonApp01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',views.itemview),
]
