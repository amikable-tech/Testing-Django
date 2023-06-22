# Generated by Django 4.2.2 on 2023-06-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('services', models.CharField(choices=[('Vaccination', 'Vaccinations'), ('Medical_Report', 'Medical Reports'), ('General_Care', 'General Care'), ('Routine_check-up_lab_test', 'Routine check-up and lab tests'), ('Other', 'Others')], default='Select', max_length=30)),
                ('subject', models.CharField(max_length=350, verbose_name='Additional information')),
                ('date_time', models.DateTimeField(verbose_name='Appointment Date')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='Patient Email Address')),
                ('booking', models.ManyToManyField(blank=True, to='main.booking')),
            ],
        ),
    ]