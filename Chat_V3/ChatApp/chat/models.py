from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse






class Room(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True,null=True)
    user = models.ManyToManyField(User, related_name="current_rooms", blank=True)
    online = models.ManyToManyField(User, blank=True)
    
    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()


    def __str__(self):
        return f"Room({self.name} {self.slug})"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
         return f'/rooms/{self.slug}/'
    
    
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField(unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    date_added = models.DateTimeField(auto_now_add=True, unique=True, null=True)

    def __str__(self):
        return f"Message({self.user} {self.room})"
    
    class Meta:
        ordering = ('date_added',)