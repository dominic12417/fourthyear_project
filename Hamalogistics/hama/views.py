from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from .models import *
from .forms import CustomerForm, CreateUserForm, vehicleForm,bookvehicleForm


# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    available_vehicles = vehicles.filter(status='available').count()
    booked_vehicles = vehicles.filter(status='booked').count()

    context = {'available_vehicles': available_vehicles, 'booked_vehicles': booked_vehicles}
    return render(request, 'hama/home.html', context)


def app_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'HAMA/login.html', context={'login_form': AuthenticationForm})

def logoutUser(request):
    logout(request)

    return redirect('login')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'hama/register.html', context)


def createVehicle(request):
    if request.method == 'POST':
        form = vehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = vehicleForm()
    context = {'form': form}
    return render(request, 'hama/vehicle.html', context)




def vehicleAvailable(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}

    return render(request, 'hama/available.html', context)

def updateAvailability(request, pk):
    vehicles = Vehicle.objects.get(id=pk)
    form = vehicleForm(instance=vehicles)

    if request.method == 'POST':
        form = vehicleForm(request.POST, instance=vehicles)
        if form.is_valid():
            form.save()
            return redirect('available')

    context = {'form': form}
    return render(request, 'hama/vehicle.html', context)

def bookVehicle(request,pk):
    vehicles=Vehicle.objects.get(id=pk)
    form=vehicleForm(instance=vehicles)

    if request.method=='POST':
        form=vehicleForm(request.POST,instance=vehicles)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'hama/book_vehicle.html',context)

def book_list(request):
    vehicles=Vehicle.objects.all()
    bvehicles=Book_Vehicle.objects.all()

    context={'bvehicles':bvehicles,'vehicles':vehicles,}
    return render(request,'hama/booking_list.html',context)

def deleteVehicle(request, pk):
    vehicles = Vehicle.objects.get(id=pk)
    if request.method == 'POST':
        vehicles.delete()
        return redirect('available')

    context = {'vehicles': vehicles}
    return render(request, ' hama/delete_vehicle.html',context)

def Booked(request):
    vehicles=Vehicle.objects.all()

    booked=vehicles.filter(status='booked')

    context = {'booked':  booked}
    return render(request, 'hama/booked.html', context)


def Available(request):
    vehicles = Vehicle.objects.all()


    available = vehicles.filter(status='available')

    context = {'available': available}
    return render(request, 'hama/availablev.html', context)