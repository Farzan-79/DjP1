from django.db import models
from django import forms
from django.conf import settings
from .utils import user_profile_upload_handler
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to=user_profile_upload_handler, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            old = UserProfile.objects.get(pk=self.pk)
        except UserProfile.DoesNotExist:
            old = None

        super().save(*args, **kwargs)

        if old and old.picture and old.picture != self.picture: #if there was a profile before, and it had a picture, and that picture is not equall to the new picture, the old picture gets deleted from the db and the instance
            old.picture.delete(save=False) #this line also deletes from the db, and save=False is because we dont need to save again, we just need a file removed
    
    def delete(self, *args, **kwargs): #this deletes the profile pictures from the db when an instance is deleted
        if self.picture:
            self.picture.delete(save=False)
        super().delete(*args, **kwargs)