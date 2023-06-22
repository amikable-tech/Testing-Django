from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from django.http import HttpResponseRedirect
# Create your views here.

def book_appointments(request):	
	submitted = False
	if request.method == "POST":
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			booking_form.save()
			return HttpResponseRedirect('/book_appointments?submitted=True')
	else:
		booking_form = BookingForm
		if 'submitted' in request.GET:
			submitted = True

	return render (request, 'main/form.html',{ 'booking_form': booking_form, 'submitted': submitted }) 

def home(request):
	return render(request, 'main/home.html', {})

