from django.shortcuts import render

# Create your views here.
def zomato(request):
    return render(request, 'home.html')

def zomato2(request):
    return render(request, 'zomato2.html')