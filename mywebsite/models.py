
from django.db import models

class signupform(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)