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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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



class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'