from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('book_appointment',views.book_appointments, name='booking'),
	path('booking_success', views.booking_success, name='booking_success'),
	path('login_user', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
	path('register_user', views.register_user, name = 'register_user'),
]
    