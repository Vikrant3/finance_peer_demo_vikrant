from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from demo_app.models import FinancePeerUserData


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been created')
            return redirect('login/')
    context = {'form': form}
    return render(request, 'demo_app/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('retrieve/')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    context = {}

    return render(request, 'demo_app/login.html', context)


def retrieve_page(request):
    finance_peer_data = FinancePeerUserData.objects.values('id', 'body', 'title', 'user_id', 'item_id')
    context = {'finance_peer_data': finance_peer_data}
    return render(request, 'demo_app/retrieve.html', context)
