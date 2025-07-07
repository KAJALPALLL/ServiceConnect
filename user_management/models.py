from django.db import models
from django.contrib.auth.models import AbstractUser

class user_profile(AbstractUser):
    phone_number = models.CharField(default=None,null=True, max_length=100)
    profession = models.CharField(default=None,null=True, max_length=100)
    description = models.CharField(default=None,null=True, max_length=100)
    address = models.CharField(default=None,null=True, max_length=100)
    profile_image = models.FileField(upload_to='user-image/',default=None,null=True)
    status = models.CharField(default='Inactive',null=True, max_length=100)

    class Meta:
        db_table = 'auth_user'