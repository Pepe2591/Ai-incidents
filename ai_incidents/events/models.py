from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PRIORITY_VALIDATOR = [MinValueValidator(1), MaxValueValidator(3)]
LONGITUDE_VALIDATORS = [MinValueValidator(-180), MaxValueValidator(180)]
CONFIDENCE_VALIDATORS = [MinValueValidator(0), MaxValueValidator(1)]
PRIORITY_VALIDATORS = [MinValueValidator(0), MaxValueValidator(10)]

# Create your models here.


class Frame(models.Model): 
    image = models.TextField()
    conf = models.FloatField() 
    detected_objects = models.TextField()


class Event(models.Model):
    "Общая модель для всех инцидентов"


    class Status(models.TextChoices): 
        NEW = 'New', 'Новый'
        IN_PROGRESS = 'In_progress', 'В прогрессе'
        RESOLVED = 'Resolved', 'Закрыт'
        FALSE_POSITIVE = 'False_posirive', 'Ложное срабатывание'
    
    class Type(models.TextChoices): 
        event = 'accident', 'collapse', 'explosion', 'fire'

    frames = models.ForeignKey(
        'Frame', 
        related_name='events_frames', 
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    event_types = models.CharField(Type.event, default=Type.event)
    
    video_url = models.URLField()
    priority = models.IntegerField(validators=PRIORITY_VALIDATOR)
    event_status = models.CharField(Status.choices, default=Status.NEW)
    
    desc = models.TextField()
    conf = models.FloatField(validators=CONFIDENCE_VALIDATORS) 

    latitude = models.FloatField(validators=LONGITUDE_VALIDATORS)
    longitude = models.FloatField(validators=LONGITUDE_VALIDATORS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name}, event_status: {self.event_status}, created_at: {self.created_at}"


class Camera(models.Model):
    camera_owner = models.CharField(max_length=100)
    status = models.BooleanField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    stream_url = models.URLField()
    coordinates = models.CharField(max_length=200)
    latitude = models.FloatField(validators=LONGITUDE_VALIDATORS)
    longitude = models.FloatField(validators=LONGITUDE_VALIDATORS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"name: {self.name} status: {self.status}"