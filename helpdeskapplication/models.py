from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Person Super User
class PersonManager(BaseUserManager):
    def create_person(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        person = self.model(email=email, **extra_fields)
        person.set_password(password)
        person.save(using=self._db)
        return person
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_person(email, password, **extra_fields)


# Person
class Person(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    firstname = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = PersonManager()

    USERNAME_FIELD = 'email'

# Asset
class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    asset_type = models.PositiveIntegerField(validators=[MaxValueValidator(1)])

    def __str__(self):
        return f"{self.asset_id} {self.user} {self.asset_type}"

# ServiceRequest
class ServiceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_description = models.CharField(max_length=255, null=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
