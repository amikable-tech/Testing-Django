from django import forms
from django.forms import ModelForm
from .models import Booking
from django.utils import timezone
from tempus_dominus.widgets import DateTimePicker
from datetime import timedelta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker 
from django.core import validators
from django.core.validators import RegexValidator



service_choices = [
('Vaccination','Vaccinations'), 
('Medical Report', 'Medical Reports'),
('General Care','General Care'),
('Routine check-up and lab test', 'Routine check-up and lab tests'),
('Other', 'Others'),
]


class BookingForm(ModelForm):
	class Meta:
		model  = Booking
		fields = "__all__"
		widgets = {
            'date_time': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                    'minDate': timezone.now().strftime('%Y-%m-%d'),
                    'maxDate': (timezone.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            )
        }
	