from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'core/home.html')

@login_required
def transaction_view(request):
    return render(request, 'core/transaction_view.html')

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
