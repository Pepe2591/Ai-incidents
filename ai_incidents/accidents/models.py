from django.db import models


# Create your models here.
class Collapse(models.Model): 
    pass 

class Fires(models.Model): 
    pass 

class Transport(models.Model): 
    pass 

class Explosion(models.Model): 
    pass 

class Category(models.Model): 
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, created: {self.created_at}" 
    
class Frame(models.Model): 
    image = models.TextField()
    conf = models.FloatField() 
    detected_objects = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_types = models.ManyToManyField('Category', related_name='events')
    frames = models.ForeignKey('Category', related_name='events', on_delete=models.CASCADE)
    video_url = models.TextField()
    priority = models.IntegerField()
    event_status = models.CharField(max_length=60)
    
    desc = models.TextField()
    conf = models.FloatField() 

    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, event_status: {self.event_status}, created_at: {self.created_at}"


class Camera(models.Model):
    camera_owner = models.CharField(max_length=100)
    status = models.BooleanField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    stream_url = models.TextField()
    coordinates = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return f"name: {self.name} status: {self.status}"
    

class Journal(models.Model): 
    pass 




