from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def SighUp(request):
    return render(request, 'SignUp.html')

def welcome(request):
    return render(request, 'welcome.html')