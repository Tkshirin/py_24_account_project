from django.contrib import admin

from applications.account.models import CustomUser, Book

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Book)