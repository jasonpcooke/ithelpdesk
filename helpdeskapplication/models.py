from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Person
class Person(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    firstname = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.user_id} {self.email} {self.password} {self.firstname} {self.surname}"

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
