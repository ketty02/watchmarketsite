from secrets import token_hex
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from activation.models import Activation
from activation.helpers.utils import send_activation_email

def inactivate_user(sender, instance, *args, **kwargs):
    if not instance.pk:
        instance.is_active = False


pre_save.connect(inactivate_user, sender=settings.AUTH_USER_MODEL)

def create_activation(sender, instance, created, *args, **kwargs):
    if created:
        activation = Activation(
            user=instance,
            token=token_hex(32)
        )
        activation.save()
        send_activation_email(activation)
post_save.connect(create_activation, sender=settings.AUTH_USER_MODEL)
