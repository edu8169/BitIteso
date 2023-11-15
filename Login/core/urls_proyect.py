from django.urls import path
from django.contrib.auth.views import LoginView  # Importa la vista de inicio de sesión de Django
from .views import home, transaction_view, register

urlpatterns = [
    path('', home, name='home'),
    path('transaction_view/', transaction_view, name='transaction_view'),
    path('register/', register, name='register'),

]
