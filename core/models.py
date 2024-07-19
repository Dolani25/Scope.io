from django.db import models

from django.db.models.functions import Lower 
from django.utils import timezone
from django.contrib.auth.models import User 
from django.utils.text import slugify
import time



# Create your models here.

# core/models.py


class Blockchain(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='coin_images' , blank=True, null=True)
    description = models.CharField(max_length=255)
    ticker = models.CharField(max_length=25)
    def __str__(self):
            return self.name
    
class Airdrop(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ticker = models.CharField(default="",max_length=25)
    legibility = models.CharField(default="",max_length=5)
    difficulty = models.CharField(default="",max_length=7)
    startprice = models.FloatField()
    blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='coin_images' , blank=True, null=True)
    contract_add = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    followers = models.IntegerField()
    integrity_score = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True,  max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # Ensure uniqueness
            counter = 1
            while Airdrop.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Task(models.Model):
    airdrop = models.ForeignKey(Airdrop, on_delete=models.CASCADE)
    description = models.TextField(blank=True , null=True)
    completed = models.BooleanField(default=False)


class FollowerProfile(models.Model):
    name = models.CharField(max_length=255)
    profile_url = models.CharField(max_length=255)
    follower_num = models.IntegerField()
    followed_airdrop = models.ManyToManyField(Airdrop)
    def __str__(self):
            return self.name
    
    
    
class ScopeUser(User):
    Email = models.EmailField(unique=True)
    whatsapp_number = models.CharField(max_length=20)
    tracked_airdrops = models.ManyToManyField(Airdrop)

class Notification(models.Model):
    user = models.ForeignKey(ScopeUser, on_delete=models.CASCADE)
    airdrop = models.ForeignKey(Airdrop, on_delete=models.CASCADE)
    message = models.TextField(blank=True , null=True)
    sent = models.BooleanField(default=False)