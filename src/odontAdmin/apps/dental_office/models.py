from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Dentist(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    specialty = models.CharField(max_length=250)


class Affliction(models.Model):
    name = models.CharField(max_length=250)


GENDERS = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
)
class Patient(models.Model):
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    place_of_birth = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDERS, max_length=250)
    address = models.CharField(max_length=250)
    specialty = models.CharField(max_length=250)
    registration_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    afflictions = models.ManyToManyField(Affliction)
    others = models.CharField(max_length=250)


class Appointment(models.Model):
    dentist = models.ForeignKey(Dentist)
    patient = models.ForeignKey(Patient)
    date = models.DateField();
    time = models.TimeField();


class Manifestation(models.Model):
    type_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)


class Examination(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)


class DentalRecord(models.Model):
    number = models.CharField(max_length=250)
    manifestations = models.ManyToManyField(Manifestation)
    examination = models.ManyToManyField(Examination)

