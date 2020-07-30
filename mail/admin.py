from django.contrib import admin

# Register your models here.
from .models import User, Email

admin.site.register(User)

class EmailAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "subject", "timestamp")

admin.site.register(Email, EmailAdmin)
