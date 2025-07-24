#signal to set the username equal to the email
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.email = instance.username
        instance.save()
        
        
@receiver(pre_save, sender=User)
def set_email_as_username(sender, instance, **kwargs):
    if instance.email and not instance.username:
        instance.username = instance.email
    elif not instance.email and instance.username:
        instance.email = instance.username
    if User.objects.filter(email=instance.email).exclude(pk=instance.pk).exists():
        raise ValueError("Email must be unique.")