from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver #add this
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=30, null=True, blank=False)
    last_name=models.CharField(max_length=30, null=True, blank=False)
    email = models.EmailField(max_length=30, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def __str__(self):
        return f'{self.user.username} Profile' 
    
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
    