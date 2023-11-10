from django.db import models
from django.db.models.functions import Length
from django.core.validators import MinLengthValidator

models.CharField.register_lookup(Length)


# The above class defines a User model with fields for username, password, and email.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username


# The Pet class represents a pet with attributes such as name, breed, age, color, description, and owner.
class Pet(models.Model):
    name = models.CharField(max_length=20)
    kind = models.TextChoices(names=('Cat', 'Dog'), value='Dog')
    breed = models.CharField(max_length=40, default="")
    age = models.IntegerField()
    color = models.CharField(max_length=40, default="")
    description = models.CharField(max_length=200, )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
