from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural="CustomUser"

    username = models.CharField(
        max_length = 20,
        help_text = "半角英数字、@/./-/+/_ で20文字に設定してください。",
        unique=True,
        #validators = [AbstractUser.username_validator],
    )

