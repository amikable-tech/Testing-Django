from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from tempus_dominus.widgets import DateTimePicker

service_choices = [
    ('', 'Select'),
    ('Vaccination', 'Vaccinations'),
    ('Medical_Report', 'Medical Reports'),
    ('General_Care', 'General Care'),
    ('Routine_check-up_lab_test', 'Routine check-up and lab tests'),
    ('Other', 'Others'),
]

class Booking(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email Address')
    phone = models.CharField('Phone Number', max_length=100)
    services = models.CharField(max_length=30, choices=service_choices, default='')
    subject = models.CharField('Additional information', max_length=350)
    date_time = models.DateTimeField()
        

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def clean(self):
        if self.services == '':
            raise ValidationError("Please select a service.")
        if self.date_time < timezone.now():
            raise ValidationError("Appointment date should be in the future.")
        if self.date_time > timezone.now() + timedelta(days=14):
            raise ValidationError("Appointment date should be within the next 14 days.")




class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('Patient Email Address')
    booking = models.ManyToManyField(Booking, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
