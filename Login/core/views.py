from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def transaction_view(request):
    return render(request, 'core/transaction_view.html')