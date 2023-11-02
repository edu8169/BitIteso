from django.urls import path
from django.contrib.auth.views import LoginView  # Importa la vista de inicio de sesión de Django
from .views import home, transaction_view, exit

urlpatterns = [
    path('', home, name='home'),
    path('transaction_view/', transaction_view, name='transaction_view'),
    path('login/', LoginView.as_view(), name='login'),  # Configura la URL de inicio de sesión
    path('logout/', exit, name='exit')
]
