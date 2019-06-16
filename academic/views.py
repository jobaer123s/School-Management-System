from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method =='POST':
        forms = UserRegisterForm(request.POST)

        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            User.objects.create_user(username, password)

            return redirect('user-login')
        else:
            context = {'forms':forms}
            return render(request, 'register.html', context)

    forms = UserRegisterForm()
    context = {'forms':forms}
    return render(request, 'register.html', context)

def user_login(request):
    return render(request, 'user_login.html')
