from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    bio = models.CharField(max_length = 120, null=True)
    profile_image = models.ImageField(upload_to='static/image', default='static/image/default_avatar.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_image.path)
        if img.mode in ("RGBA", "P"): 
            img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    def __str__(self):
        return self.user


class Post(models.Model):
    profile_post = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post_image = models.ImageField(upload_to='static/image')
    post_description = models.CharField(max_length = 500)
    post_time = models.DateTimeField(null=True)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.post_image.path)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.post_image.path)
    
    def __str__(self):
        return self.post_description


class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comm')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comm')
    comment = models.CharField(max_length=400)

    def __str__(self):
        return self.comment[:60]
