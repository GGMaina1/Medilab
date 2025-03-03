from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=59)
    email = models.EmailField()
    status = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    #create a staff model
    #save  firstname,lastname,position,phonenumber-charfield,email,hiredate
    #should return firstname and lastname
class Staff(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname


    #create a ward model
    #name,total beds, available beds
    #save by return the name
class Ward(models.Model):
    name = models.CharField(max_length=50)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name