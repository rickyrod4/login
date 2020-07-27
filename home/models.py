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

    def athenticate(self, email, password):
        users_with_email = self.filter(email=email)
        if not users_with_email:
            return False
        user = users_with_email[0]
        return bcrypt.checkpw(password.encode(),user.password.encode())

    def validate(self, form_data):
        errors = {}
        if len(form_data['first_name']) < 1:
            errors['first_name'] = "First Name Field Is Required"
        if len(form_data['last_name']) < 1:
            errors['last_name'] = "Last Name Field Is Required"
        if len(form_data['email']) < 1:
            errors['email'] = "Email Field Is Required"
        if len(form_data['password']) < 1:
            errors['password'] = "Password Field Is Required"
        if len(form_data['confirmPassword']) < 1:
            errors['confirmPassword'] = "Must Confirm Password"

        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    objects = UserManager()
