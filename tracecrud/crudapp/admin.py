from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','rating','review']