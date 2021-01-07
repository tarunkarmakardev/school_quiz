from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registerUser/', views.registerUser, name = 'registerUser'),
    path('loginUser/', views.loginUser, name = 'loginUser'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
]