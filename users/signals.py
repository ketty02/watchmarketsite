from users.models import MyUser, Profile
from django.db.models.signals import pre_save, post_save
from helpers.emails import send_register_email
from users.models import MyUserManager


def generate_random_password(sender, instance, *args, **kwargs):
    if not instance.pk:
        email = instance.email
        first_name = instance.first_name
        last_name = instance.last_name

        generated_password = MyUserManager().make_random_password()
        send_register_email(first_name, last_name, email, generated_password)

        instance.set_password(generated_password)



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

pre_save.connect(generate_random_password, sender=MyUser)
post_save.connect(create_user_profile, sender=MyUser)
