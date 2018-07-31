from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


# Create your models here.

#
# ROLES MODEL
#
class Roles(models.Model):
    
    name = models.CharField(max_length = 20, db_index = True, unique = True,)
    is_active = models.BooleanField(default = True, db_index = True,)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name_plural = "roles_table"
        ordering = ['pk']


#
# Custom User Model. Extended from the default user model
#
class CustomUser(AbstractUser):

    #
    # Title Choices
    #
    title_choices = (('Mr','Mr'),('Mrs','Mrs'),('Miss','Miss'),('Ms','Ms'),('Sir','Sir'),('Dr','Dr'))

    #
    # Gender Choices
    #
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    gender_choices = ((MALE,'Male'),(FEMALE, 'Female'), (OTHERS, 'Others')) 

    #
    # Marital Status Choices
    #
    marital_status_choices = (("Single", "Single"),
                                ("Married", "Married"),
                                ("Divorced", "Divorced"),
                                ("Separated", "Separated"),
                                ("Living With Partners", "Living With Partners"),
                                ("Widowed", "Widowed"))
                                
    #
    # Model Structure
    #
    role = models.ForeignKey('Roles', db_index = True, null = True, blank = True, on_delete = models.SET_NULL,)
    dob = models.DateField(null = True, blank = True, db_index = True,)
    phone = models.CharField(max_length = 100, blank = True, null = True,)
    title = models.CharField(max_length = 4, db_index = True, blank = True, null = True, choices = title_choices, default = 'Mr')
    gender = models.CharField(max_length = 1, db_index = True, default = MALE, choices = gender_choices, blank = True, null = True,)
    marital_status = models.CharField(max_length = 40, db_index = True, default = 'Single', blank = True, null = True, choices = marital_status_choices,)
    email = models.EmailField(blank = True, null = True, db_index = True,)
    postcode = models.CharField(max_length = 10, null = True, blank = True, db_index = True,)
    city = models.CharField(max_length = 30, null = True, blank = True, db_index = True,)
    state = models.CharField(max_length = 30, null = True, blank = True, db_index = True,)
    address_line_1 = models.CharField(max_length = 100, null = True, blank = True, db_index = True,)
    address_line_2 = models.CharField(max_length = 100, null = True, blank = True,)
    country = models.CharField(max_length = 30, null = True, blank = True, db_index = True,)
    acknowledge = models.BooleanField(default = True, db_index = True)
    sponsor = models.BooleanField(default = True, db_index = True)
    income = models.FloatField(default = 0, db_index = True,)
    home_owner = models.BooleanField(default = False, db_index = True,)
    browser = models.CharField(max_length = 250, null = True, blank = True, db_index = True,)
    bversion = models.CharField(max_length = 250, null = True, blank = True, db_index = True,)
    platform = models.TextField(null = True, blank = True,)
    ip_address = models.CharField(max_length = 20, null = True, blank = True,)
    extra_fields = models.TextField(null = True, blank = True,)
    inserted_date = models.DateTimeField(auto_now = False, auto_now_add = True, db_index = True,)
    modified_date = models.DateTimeField(auto_now = True, null = True, blank = True, db_index = True,)





    