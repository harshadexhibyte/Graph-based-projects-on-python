from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('UserDashboard',views.Dashboard,name='Dashboard'),
    path('FileUploded',views.FileUploded,name='FileUploded'),
    path('download',views.download,name='download'),
    path('LogOut',views.LogOut,name='LogOut'),
]
