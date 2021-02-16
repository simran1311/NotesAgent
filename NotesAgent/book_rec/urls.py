from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import login

app_name = 'book_rec'

urlpatterns = [
    url('^$', views.books,name='books'),

    url('^(?P<book_id>[0-9]+)$', views.detail, name='detail'),

    url('^register/$', views.UserFormView.as_view(), name='register'),

    url('^home/$', TemplateView.as_view(template_name='book_rec/home.html'), name='home'),

    url('^add/$', views.BookInput.as_view(), name='BookAdd'),

    url('^notes/$', views.notes,name='notes'),

    url('^gpa/$', TemplateView.as_view(template_name='book_rec/gpa.html'), name='gpa'),

    url('^about/$', TemplateView.as_view(template_name='book_rec/about.html'), name='about'),

    url('^login/$', views.login, name='login'),

    url('^course/$', TemplateView.as_view(template_name='book_rec/Category.html'), name='category'),

    url('^logout/$', views.logout,  name='logout'),

    url('^note_cat/$', TemplateView.as_view(template_name='book_rec/note.html'), name='note_cat'),
]
