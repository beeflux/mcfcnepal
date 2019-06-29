from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def userregisterform(request):
    form = UserCreationForm()
    return render(request, 'authentication/register.html',{'form':form})