from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Saving the user sets a signal to the receiver, 
# which creates and saves a profile automatically using the methods above.
# The Django documentation sugests a creation of the signals.py file
# to set the signals, although some people put this in the 
# models (not recommended).