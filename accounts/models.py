from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Profile for {user}'.format(user=self.user)


@receiver(post_save, sender=User)
def user_profile_create_or_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


