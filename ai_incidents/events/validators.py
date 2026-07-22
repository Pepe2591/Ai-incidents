from rest_framework.serializers import ModelSerializer, ValidationError 
from .models import Event 
 
class EventsModelSerializer(ModelSerializer): 
    
    class Meta: 
        model = Event
        fields = '__all__' 


    def validate_snapshot(self, value : str): 
        if value.name.endswith((".jpg", ".png", ".heic", ".heif")): 
            return value 
        else: 
            return ValidationError('Invalid snapshot')
    