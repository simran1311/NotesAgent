from django.db import models
from django.urls import reverse
# Create your models here.


sub_choice= [
        ('TOC','Theory of Computation'),
        ('SEDP','Software Engineering and Development'),
        ('A.Maths','Applied Mathematics'),
        ('A.Physics','Applied Physics'),
        ('EEE/BEE','Elements of Electrical Engineering'),
        ('ECP','Elements of Computer Engineering'),
        ('DEC','Digital Electronics And Communication'),
        ('STQA','Software Testing and Quality Assuarance'),
        ('AppChem','Applied Chemistry'),
        ('EVS','Environmental Studies'),
        ('AutoCAD','AutoCAD'),
        ('CAO','Computer Architecture and Organization'),
        ('DS','Discrete Structure'),
        ('DSA','Data Structure and Algorithm'),
        ('DBMS','DataBase Management System'),
        ('OOPS','Object Oriented and Programming System'),
        ('ADA','Analysis And Design of Algorithm'),
        ('MPI','MicroProcessor and Interfacing'),
        ('JAVA','Core Java'),
        ('POS','Principal of Operating System'),
        ('CG','Computer Graphics'),
        ('AJava','Advance Java'),
        ('WTCS','Web Technology and Cyber Security'),
    ]


class BookRecd(models.Model):
    subject= models.CharField(choices=sub_choice, max_length=6)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    year_b = models.CharField(max_length=100)
    book_p = models.FileField()
    book_url = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('book_rec:detail', kwargs={'book_id':self.pk} )


    def __str__(self):
        return str(self.pk) + ' - ' + self.book_url + ' - ' + self.name + ' - ' + self.author


class NotesRecd(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.title + ' - ' + self.subject
