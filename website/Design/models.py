from django.db import models
from django.db.models import Model
from datetime import datetime
# Create your models here.

class Register(models.Model):

    choice = {
        ("student","student"),
        ("faculty","faculty"),
        ("hod","hod")
    }
    
    name = models.CharField(max_length=1000,blank=False)
    authority = models.CharField(max_length=10,choices=choice,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False)
    phone = models.IntegerField(blank=False)
    address = models.CharField(max_length=1000,blank=False)
    date = models.DateField(default=datetime.now())

    def __str__(self) -> str:
        return f"ID - {self.id} | Name - {self.name} | Authority - {self.authority} | Email - {self.email} | Password - {self.password} | Phone Number - {self.phone} | Address - {self.address} | Date of Creation - {self.date}"

class Student(models.Model):
    regis = models.OneToOneField(Register,on_delete=models.CASCADE)
    Class = models.CharField(max_length=10,blank=False)
    section = models.CharField(max_length=1,blank=False)

    def __str__(self) -> str:
        return f"Name - {self.regis.name} | Authority - {self.regis.authority} | Email - {self.regis.email} | Password - {self.regis.password} | Phone - {self.regis.phone} | Address - {self.regis.address} | Date - {self.regis.date} | Class - {self.Class} | Section -{self.section}"

class Faculty(models.Model):
    regis = models.OneToOneField(Register,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50,blank=False)

    def __str__(self) ->str:
        return f"ID - {self.id} | Name - {self.regis.name} | Authority - {self.regis.authority} | Email - {self.regis.email} | Password - {self.regis.password} | Address - {self.regis.address} | Phone Number - {self.regis.phone} | Date - {self.regis.date} | Qualification - {self.qualification}"
        
class Link(models.Model):
    teacher = models.CharField(max_length=1000,blank=False)
    Class = models.CharField(max_length=100,blank=False)
    section = models.CharField(max_length=1,blank=False)
    link = models.CharField(max_length=100,blank=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f"Name of the Faculty - {self.teacher} | Class - {self.Class} | Section - {self.section} | Link - {self.link} | Date - {self.date}"

class Questions(models.Model):
    teacher = models.CharField(max_length=1000,blank=False)
    Class  = models.CharField(max_length=15,blank=False)
    section = models.CharField(max_length=1,blank=False)
    question = models.CharField(max_length=1000,blank=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f"Faculty - {self.teacher} | Class - {self.Class} | Section - {self.section} | Question - {self.question} | Date - {self.date}"

class Answers(models.Model):
    
    faculty = models.CharField(max_length=1000,blank=False)
    question = models.CharField(max_length=1000,blank=False)
    student = models.CharField(max_length=1000,blank=False)
    Class = models.CharField(max_length=1000,blank=False)
    section = models.CharField(max_length=1,blank=False)
    date = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=20,blank=False)
    file = models.FileField(upload_to="media/",blank=True)

    def __str__(self) -> str:
        return f"Faculty - {self.faculty} | Question - {self.question} | Submitted By - {self.student} | Class - {self.Class} | Section - {self.section} | File - {self.file} | Date of Submission - {self.date} | Status - {self.status}"

class Allotment(models.Model):

    name = models.CharField(max_length=100,blank=False)
    Class = models.CharField(max_length=10,blank=False)
    section = models.CharField(max_length=1,blank=False)
    subject = models.CharField(max_length=100,blank=False)

    def __str__(self) -> str:
        return f"Name - {self.name} | Class - {self.Class} | Section - {self.section} | Subject - {self.subject}"

class Notice(models.Model):

    name  = models.CharField(max_length=100,blank=False)
    notice  = models.CharField(max_length=1000,blank=False)
    Class  = models.CharField(max_length=10,blank=False)
    section = models.CharField(max_length=1,blank=False) 
    date  = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f"Name - {self.name} | Notice - {self.notice} | Class - {self.Class} | Section - {self.section} | Date - {self.date}"

class Message(models.Model):
    sender = models.CharField(max_length=100,blank=False)   
    receiver = models.CharField(max_length=100,blank=False)
    Class = models.CharField(max_length=10,blank=True)
    section = models.CharField(max_length=1,blank=True)
    message = models.CharField(max_length=1000,blank=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f"Sender - {self.sender} | Receiver - {self.receiver} | Class - {self.Class} | Section - {self.section} | Message - {self.message} | Date - {self.date}"

class Query(models.Model):
    name = models.CharField(max_length=100,blank=False)
    faculty = models.CharField(max_length=100,blank=False)
    Class = models.CharField(max_length=25,blank=False)
    section  = models.CharField(max_length=1,blank=False)
    query = models.CharField(max_length=1000,blank=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f"Name of the Student - {self.name} | Name of the Faculty - {self.faculty} | Query - {self.query} | Class - {self.Class} | Section - {self.section} | Date - {self.date}"