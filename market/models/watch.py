from django.db import models
from django.conf import settings

class Watch(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='watches')
    name = models.CharField(max_length=255)
    brand_picture = models.FileField(upload_to='brand', null=True)


    class Meta:
        verbose_name = "Watch"
        verbose_name_plural = "Watches"

    def __str__(self):
        return self.name
