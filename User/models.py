from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default=None)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique=True, null=True)

    class Meta:
        unique_together = ('email', 'username')
