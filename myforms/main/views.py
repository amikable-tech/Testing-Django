from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect ('home')
		else:
			messages.success = (request, ("Invalid username or password, verify details and login again."))
			return redirect('login')
	else: 
		return render(request, 'registration/login.html', {})
     


def logout_user(request):
	logout(request)
	messages.success(request, ("Logout request successful!"))
	return redirect('main/home.html')

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration successful, please login!"))
			return redirect('main/home.html')
	else:
		form = RegisterUserForm()
	return render(request, 'main/register.html', {
		'form':form,
		})


	
def book_appointments(request):	
	submitted = False
	if request.method == "POST":
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			booking_form.save()
			return HttpResponseRedirect('booking_success')
	else:
		booking_form = BookingForm()
		if 'submitted' in request.GET:
			submitted = True
	return render (request, 'main/form.html', { 'booking_form': booking_form, 'submitted': submitted }) 


def booking_success(request):
	return render(request, 'main/successful.html')

	
def home(request):
	return render(request, 'main/home.html', {})

