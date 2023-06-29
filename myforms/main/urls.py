from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
	path('', views.home, name='home'),
	path('book_appointment',views.book_appointments, name='booking'),
	path('booking_success', views.booking_success, name='booking_success'),
	path('login_user', CustomLoginView.as_view(template_name='registration/login.html'), name = 'login'),
	path('register_user', views.register_user, name = 'register_user'),
	
]
    