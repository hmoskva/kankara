import random
import os

from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save

from kankara.utils import unique_slug_generator


def get_filename_ext(filepath):
    """
        Method to split file path into corresponding name and extension
    """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    """
        Method to customize filename using random number and file extension
    """
    new_file_name = random.randint(1, 8679876779)
    name, ext = get_filename_ext(filename)
    final_file_name = '{new_file_name}{ext}'.format(new_file_name=new_file_name, ext=ext)
    return 'businesses/{new_file_name}/{final_file_name}'.format(
        new_file_name=new_file_name, final_file_name=final_file_name)


class Business(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('businesses:details', kwargs={'id': self.id})


@receiver(pre_save, sender=Business)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
