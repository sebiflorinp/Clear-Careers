from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, is_employer, is_employee, password=None):

        if not email:
            return ValueError('Email is a required value.')
        if not password:
            return ValueError('password is a required value.')
        if not is_employee and not is_employer:
            return ValueError('the user needs to be an employee or an employer')
        if is_employer == is_employee:
            return ValueError('the user cannot be an employer and an employee at the same time.')

        email = self.normalize_email(email)
        user = self.model(email=email, is_employee=is_employee, is_employer=is_employer)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True, blank=False, null=False)
    is_employer = models.BooleanField(default=False, blank=False, null=False)
    is_employee = models.BooleanField(default=False, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_employer', 'is_employee']

    objects = UserManager()

    def __str__(self):
        return self.email