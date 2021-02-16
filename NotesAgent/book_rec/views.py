from django.shortcuts import render, redirect
from django.http import Http404
from .models import BookRecd, NotesRecd
from django.template import loader
from django.contrib.auth import authenticate
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import auth
from django.contrib import messages


# Create your views here.


def books(request):
    all_books = BookRecd.objects.all()
    context = {'all_books': all_books,}
    return render(request, 'book_rec/index.html', context)


def home(request):
    context = {""}
    return render(request, 'book_rec/home.html', context)


def detail(request, book_id):
    try:
        book = BookRecd.objects.get(pk=book_id)
    except BookRecd.DoesNotExist:
         raise Http404("NO Book")
    return render(request, 'book_rec/detail.html', {'book': book})


class UserFormView(View):
    form_class = UserForms
    template_name = 'book_rec/regForm.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('book_rec:home')

        return render(request, self.template_name, {'form': form})


class BookInput(CreateView):
    model = BookRecd
    #form_class = BookRecdForm
    fields = ['name', 'author', 'subject', 'year_b', 'book_p', 'book_url']


def notes(request):
    all_notes = NotesRecd.objects.all()
    context = {'all_notes': all_notes,}
    return render(request, 'book_rec/books.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('book_rec:home')
        else:
                messages.info(request, 'Invalid Credentials')
                return redirect('book_rec:login')
    else:
        return render(request, 'book_rec/login.html')


def logout(request):
    auth_logout(request)
    return redirect('book_rec:home')