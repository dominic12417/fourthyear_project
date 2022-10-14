from django.urls import path

from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.app_login, name='login'),
    path('register/', views.register, name='register'),
    path('vehicle/', views.createVehicle, name='vehicle'),
    path('available', views.vehicleAvailable, name='available'),
    path('update_availability/<str:pk>/', views.updateAvailability, name='update_availability'),
    path('availablev', views.Available, name='availablev'),
    path('booked', views.Booked, name='booked'),
    path('logout', views.logoutUser, name='logout'),
    path('delete_vehicle/<str:pk>/', views.deleteVehicle,name='delete_vehicle'),
    path('book_vehicle/<str:pk>/',views.bookVehicle,name='book_vehicle'),
    path('bookList/',views.book_list,name='bookList')

]