from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
import requests

def home(request):
    return render(request, 'core/home.html')

@login_required
def transaction_view(request):
    # URL del servidor externo
    url = "http://127.0.0.1:5000/get_blockchain"

    # Realiza la solicitud HTTP
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
    except requests.RequestException as e:
        # Manejar errores de la solicitud aquí
        datos = {}
        print(e)  # Puedes cambiar esto por un manejo de errores más sofisticado

    # Pasar los datos obtenidos a la plantilla
    return render(request, 'core/transaction_view.html', {'datos': datos})

def register(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()  # Guardar el usuario

            # Obtener los datos limpios directamente del formulario
            username = user_creation_form.cleaned_data.get('username')
            password = user_creation_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        user_creation_form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': user_creation_form})
