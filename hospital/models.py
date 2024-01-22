from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usertype = models.CharField(max_length=20)


class Doctor(models.Model):
    doctor_id =models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    department = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    status=models.BooleanField(default=False)

class Patient(models.Model):
    patient_id =models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    symptoms = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    status=models.BooleanField(default=False)
    assignedDoctorID =models. PositiveIntegerField( null=True)

class Appointment(models.Model):
    patientID=models.PositiveIntegerField(null=True)
    doctorID=models.PositiveIntegerField(null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)