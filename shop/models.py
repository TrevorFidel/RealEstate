from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname