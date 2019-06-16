from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SchoolInfo(models.Model):
    school_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name
