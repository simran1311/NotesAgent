from django.contrib import admin
from .models import BookRecd, NotesRecd


@admin.register(BookRecd)
class AdminBookRecd(admin.ModelAdmin):
    pass


@admin.register(NotesRecd)
class AdminNotesRecd(admin.ModelAdmin):
    pass
