# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class MyUser(AbstractUser):
    created_at = models.DateTimeField(
        _("Creation date"),
        default=timezone.now,
        editable=False
    )
