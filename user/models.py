from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=10,null=True,blank=True)
    is_register_staff = models.BooleanField(default=False)
    is_duel_staff = models.BooleanField(default=False)
    is_arbiter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
