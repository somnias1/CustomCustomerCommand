from django.db import models

from django.db import models


class Customer(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    company = models.CharField(max_length=150)
    title = models.CharField(max_length=225)
    city = models.CharField(max_length=150)

    def clean(self):
        gender = ["Male", "Female"]
        if self.gender not in gender:
            raise ValidationError("Gender not valid")
        super().clean()
