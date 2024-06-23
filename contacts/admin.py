from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_editable = ('last_name', 'email')
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('email',)


admin.site.register(Contact, ContactAdmin)
