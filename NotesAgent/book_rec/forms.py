from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from book_rec.models import BookRecd


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


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UserFormsLin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


#class BookRecdForm(ModelForm):
    #subject = forms.ChoiceField(choices=sub_choice, required=True )
    #class Meta:
        #model = BookRecd
        #widgets = {'subject': forms.TextInput(attrs={'placeholder': 'Subject:'}),
        #}

