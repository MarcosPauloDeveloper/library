from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name