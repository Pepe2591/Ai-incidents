from django.db import models

# Create your models here.

class Camera(models.Model):
    status = models.BooleanField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    stream_url = models.TextField()
    cur_event_id = models.ForeignKey('Dangerous_event', related_name = 'Camera', on_delete = models.CASCADE)
    width = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"name: {self.name} status: {self.status}"

class Category(models.Model): 
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, desc: {self.desc}" 

class Dangerous_event(models.Model):
    name = models.CharField(max_length=100)
    url_img = models.TextField()
    url_video = models.TextField()
    event_status = models.CharField()
    event_type_id = models.ForeignKey(Category, related_name='Dangerous_event', on_delete=models.CASCADE)
    width = models.FloatField()
    longitude = models.FloatField()
    priority = models.IntegerField()
    promt = models.TextField()
    conf = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name}, event_status: {self.event_status}, created_at: {self.created_at}"