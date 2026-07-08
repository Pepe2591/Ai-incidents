from django.db import models


# Create your models here.


class Category(models.Model): 
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, desc: {self.desc}" 
    
class Dangerous_event(models.Model):
    name = models.CharField(max_length=100)
    categorys = models.ManyToManyField('Category', related_name='dangerous_events')
    priority = models.IntegerField()
    url_img = models.TextField()
    url_video = models.TextField()
    event_status = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    desc = models.TextField()
    conf = models.FloatField() 
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, event_status: {self.event_status}, created_at: {self.created_at}"

class Camera(models.Model):
    status = models.BooleanField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    stream_url = models.TextField()
    width = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"name: {self.name} status: {self.status}"



