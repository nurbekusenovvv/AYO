from django.shortcuts import render, redirect
from django.contrib import messages
from .forms.py import UserRegisterForm # type: ignore

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
