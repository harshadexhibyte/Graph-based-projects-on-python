from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('UserDashboard',views.Dashboard,name='Dashboard'),
    path('FileUploded',views.FileUploded,name='FileUploded'),
    path('UserProfile',views.UserProfile,name='UserProfile'),
    path('Download',views.Download,name='Download'),
    path('LogOut',views.LogOut,name='LogOut'),
]
