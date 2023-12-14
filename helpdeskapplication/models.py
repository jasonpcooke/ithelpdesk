from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Person
class Person(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    firstname = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    isadmin = models.BooleanField(default=False)

# Asset
class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Person)
    asset_type = models.PositiveIntegerField(validators=[MaxValueValidator(1)])

# Request
class ServiceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_description = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(Person)
    asset = models.ForeignKey(Asset)
