from django.db import models
from django.db.models.functions import Length
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

models.CharField.register_lookup(Length)
models.EmailField.register_lookup(Length)


class User(models.Model):
    """
    The User class represents a user model with fields for username, password, and email. It includes
    validation rules and constraints to ensure that the fields have valid values.
    Example Usage
    user = User(username="testuser", password="password123", email="testuser@example.com")
    if user.full_clean():
        user.save()

    Methods
    __str__(): Returns a string representation of the user, which is the username.
    save(): Saves the user instance to the database.
    delete(): Deletes the user instance from the database.

    Fields
    username: CharField with a maximum length of 40 characters. Represents the username of the user.
    password: CharField with a maximum length of 16 characters. Represents the password of the user.
              Includes validation rules for minimum length, maximum length, and allowed characters.
    email:    EmailField with a maximum length of 100 characters. Represents the email of the user.
              Includes validation rules for minimum length, maximum length, and email format.
    """
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


class Pet(models.Model):
    """The Pet class represents a pet with various attributes such as name, kind, breed, age, color, description,
    and owner. It includes constraints to ensure that certain fields have valid values, such as minimum length for
    name and breed, positive age, and non-empty values for color and description. The Pet class also has a unique
    constraint that ensures the combination of name and owner is unique, preventing duplicate pets with the same name
    and owner.

    #Creating a pet instance
    pet = Pet(name="Fluffy", kind=KindChoices.Cat, breed="Persian", age=3, color="White",
              description="Cute cat", owner=user)
    if pet.full_clean():
        pet.save()

    Methods
    __str__(): Returns a string representation of the pet, which is the pet's name.
    save(): Saves the pet instance to the database.
    delete(): Deletes the pet instance from the database.
    full_clean(): Validates the pet instance against the defined constraints.

    Fields
    name: CharField with a maximum length of 20 characters. It represents the name of the pet.
    kind: CharField with a maximum length of 10 characters. It represents the kind of the pet (e.g., Cat or Dog).
    breed: CharField with a maximum length of 40 characters. It represents the breed of the pet.
    age: PositiveIntegerField. It represents the age of the pet.
    color: CharField with a maximum length of 40 characters. It represents the color of the pet.
    description: CharField with a maximum length of 200 characters. It represents the description of the pet.
    owner: ForeignKey to the User model. It represents the owner of the pet."""

    name = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    kind = models.CharField(max_length=10, choices=KindChoices.choices, default=KindChoices.Dog)
    breed = models.CharField(max_length=40, default="Unknown", )
    age = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=40, default="Unknown", )
    description = models.CharField(max_length=200, default='Not given')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

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
