from django.contrib import admin
from core.models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
