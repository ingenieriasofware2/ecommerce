from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'access/home.html')

def products(request):
    return render(request, 'access/products.html')