from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def transaction_view(request):
    return render(request, 'core/transaction_view.html')

def exit(request):
    logout(request)
    return redirect('home')
