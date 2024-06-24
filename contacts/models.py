from django.utils.timezone import datetime

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SharedContact(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, related_name='shared_contacts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contact.first_name} shared with {self.shared_with.last_name}"
