from django.contrib import admin

from .models import Subject, Course, URL

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(URL)
