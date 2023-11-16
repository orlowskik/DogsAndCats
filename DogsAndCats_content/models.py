from django.db import models
from django.db.models.functions import Length
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator

models.CharField.register_lookup(Length)
models.EmailField.register_lookup(Length)


# The above class defines a User model with fields for username, password, and email, along with validation rules and
# constraints.
class User(models.Model):
    username = models.CharField(max_length=40, validators=[MinLengthValidator(1)], unique=True)
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16),
                                                           RegexValidator(r'^\b[a-zA-Z]+[a-zA-Z\d_.@!#$%^&*?-]*\b$')])
    email = models.EmailField(max_length=100,
                              unique=True,
                              validators=[MinLengthValidator(5),
                                          RegexValidator(r'\b[a-zA-Z]+[a-zA-Z\d_.-]*@[a-zA-Z]+\.[a-zA-Z]+\b$')])

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


class KindChoices(models.TextChoices):
    Cat = 'Cat', 'Cat'
    Dog = 'Dog', 'Dog'


# The Pet class represents a pet with attributes such as name, breed, age, color, description, and owner.
class Pet(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    kind = models.CharField(max_length=10, choices=KindChoices.choices, default=KindChoices.Dog)
    breed = models.CharField(max_length=40, default="Unknown",)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    color = models.CharField(max_length=40, default="Unknown",)
    description = models.CharField(max_length=200, default='Not given')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(name__length__gte=1),
                                   name="Name must be at least 1 character"),
            models.CheckConstraint(check=models.Q(breed__length__gte=1),
                                   name="Breed must be at least 1 character"),
            models.CheckConstraint(check=models.Q(age__gte=0),
                                   name="Age must be positive"),
            models.CheckConstraint(check=models.Q(color__length__gte=1),
                                   name="Color must be at least 1 character"),
            models.CheckConstraint(check=models.Q(description__length__gte=1),
                                   name="Description must be at least 1 character"),
            models.UniqueConstraint(fields=['name', 'owner'],
                                    name='Unique name and owner for a pet')
            ]
