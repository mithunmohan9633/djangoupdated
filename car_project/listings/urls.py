from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('signup/', views.user_registration, name='signup'),  # User registration
    path('login/', views.user_login, name='login'),  # User login
    path('logout/', views.user_logout, name='logout'),  # User logout
    
    # Car for Sale URLs
    path('add-car-for-sale/', views.add_car_for_sale, name='add_car_for_sale'),  # Add new car for sale
    path('my-cars-for-sale/', views.list_my_cars, name='list_my_cars'),  # List user's cars for sale
    path('cars-for-sale/', views.list_cars_for_sale, name='list_cars_for_sale'),  # List all cars for sale
    path('cars-for-sale/<int:car_id>/', views.car_for_sale_detail, name='car_for_sale_detail'),  # Car detail view
    path('cars-for-sale/<int:car_id>/edit/', views.car_for_sale_edit, name='edit_car_for_sale'),  # Edit car for sale
    path('cars-for-sale/<int:car_id>/delete/', views.delete_car_for_sale, name='delete_car_for_sale'),  # Delete car for sale
    
    # Car for Rent URLs
    path('add-car-for-rent/', views.add_car_for_rent, name='add_car_for_rent'),  # Add new car for rent
    path('my-cars-for-rent/', views.list_my_rent_cars, name='list_my_rent_cars'),  # List user's cars for rent
    path('cars-for-rent/', views.list_cars_for_rent, name='list_cars_for_rent'),  # List all cars for rent
    path('cars-for-rent/<int:car_id>/', views.car_for_rent_detail, name='car_for_rent_detail'),  # Car detail view for rent
    path('cars-for-rent/<int:car_id>/edit/', views.car_for_rent_edit, name='edit_car_for_rent'),  # Edit car for rent
    path('cars-for-rent/<int:car_id>/delete/', views.delete_car_for_rent, name='delete_car_for_rent'),  # Delete car for rent
]
