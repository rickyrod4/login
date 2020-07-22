from django.db import models
import bcrypt
import re


class UserManager(models.Manager):
    def register(self, form_data):
        password = form_data['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.create(
            first_name=form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = pw_hash
        )

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    objects = UserManager()
