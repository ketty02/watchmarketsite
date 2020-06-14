from django.db import models
from django.conf import settings

class Watch(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name
