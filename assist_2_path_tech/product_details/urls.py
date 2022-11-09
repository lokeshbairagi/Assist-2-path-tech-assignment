from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
    path('update/<int:id>/',views.update_product,name='update_product'),
    path('search/<int:id>/',views.search,name='search'),
]