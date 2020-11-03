import cursor as cursor
import username
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from model_utils import Choices
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import MySQLdb
import mysql.connector



CHOICES_GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ('NA', 'Decline to State')
)

CHOICES = (
    ('M', 'Married'),
    ('D', 'Divorced'),
    ('S', 'Separated'),
    ('SN', 'Single'),
)

CHOICES_CURRENCY = (
    ('INR', 'INR'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('JPY', 'JPY'),
    ('GBP', 'GBP'),
    ('AUD', 'AUD'),
    ('CAD', 'CAD'),
    ('CHF', 'CHF'),
    ('CNY', 'CNY'),
    ('HKD', 'HKD'),
    ('NZD', 'NZD'),

)


class Employee(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(max_length=254, default='Enter valid email.')
    company_name = models.ManyToManyField("Company", blank=True)
    salary = models.CharField(max_length=10, null=True)
    currency = models.TextField(choices=CHOICES_CURRENCY, null=True)
    pan = models.CharField(max_length=10, default='AAA0000000')
    gender = models.TextField(choices=CHOICES_GENDER, null=True)
    marital_status = models.TextField(choices=CHOICES, null=True)
    address_1 = models.CharField(default="Address Line 1", max_length = 1024)
    address_2 = models.CharField(default="Address Line 2", max_length = 1024)
    city = models.TextField(default="City")
    state = models.TextField(default="State")
    pin_code = models.CharField(max_length=10, default="0000000000" )
    country = models.TextField(default="Country")


    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name_plural = "Employees"



class Company(models.Model):
    company = models.TextField()

    def __str__(self):
        return f"{self.company}"

    class Meta:
        verbose_name_plural = "Companies"


