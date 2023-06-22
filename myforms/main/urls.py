from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('book_appointment',views.book_appointments, name='booking'),
	path('booking_success', views.booking_success, name='booking_success')
]
    