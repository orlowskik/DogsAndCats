from django.db import models
from django.db.models.functions import Length
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

import re

models.CharField.register_lookup(Length)
models.EmailField.register_lookup(Length)


# The above class defines a User model with fields for username, password, and email.
class User(models.Model):
    username = models.CharField(max_length=40, validators=[MinLengthValidator(1)], unique=True)
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16)])
    email = models.EmailField(max_length=100, unique=True, validators=[MinLengthValidator(5)])

    def clean(self):
        if not re.match(r'^\b[a-zA-Z]+[a-zA-Z\d_.@!#$%^&*?-]*\b$', self.password):
            raise ValidationError("Passwords cannot contain whitespace and brackets")
        if not re.match(r'^\b[a-zA-Z]+[a-zA-Z\d_.-]*@[a-zA-Z]+\.[a-zA-Z]+\b$', self.email):
            raise ValidationError("Email has to be a valid email address")

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(username__length__gte=1),
                                   name="Username must be at least 1 character"),
            models.CheckConstraint(check=models.Q(password__length__gte=8),
                                   name="Password must be at least 8 characters"),
            models.CheckConstraint(check=models.Q(email__length__gte=5),
                                   name="Email must be at least 5 character"),
        ]

    def __str__(self):
        return self.username


# The Pet class represents a pet with attributes such as name, breed, age, color, description, and owner.
class Pet(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    kind = models.TextChoices(names=('Cat', 'Dog'), value='Dog')
    breed = models.CharField(max_length=40, default="")
    age = models.IntegerField(default=0)
    color = models.CharField(max_length=40, default="")
    description = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
