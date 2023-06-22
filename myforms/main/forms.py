from django import forms
from django.forms import ModelForm
from .models import Booking, Patient
from django.utils import timezone
from tempus_dominus.widgets import DateTimePicker
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
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
        model = Booking
        fields = '__all__'
        widgets = {
            'date_time': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                    'minDate': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
                    'maxDate': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
                    'disabledTimeIntervals': [
                        [datetime(1900, 1, 1, 12, 0).strftime('%H:%M'), datetime(1900, 1, 1, 13, 30).strftime('%H:%M')],
                    ],
                    'daysOfWeekDisabled': [0, 6],  
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            )
        }

