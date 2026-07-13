from rest_framework.serializers import ModelSerializer, ValidationError 
from .models import Event 
 
class EventsModelSerializer(ModelSerializer): 

    allowed_events = ["smoke", "fire", "explosion", 
                      "collapse", "traffic_accident", "fires"]
    class Meta: 
        model = Event
        fields = '__all__' 


    def validate_categorys(self, value): 
        pass

    def validate_longitude(self, value): 
        if value == None: 
            return self.Meta.mode
        if value > 180: 
            return ValidationError('The longitude cannot be more than 180!')

    def validate_latitude(self, value): 
        if value > 90: 
            return ValidationError('The latitude cannot be more than 90!')

    def validate_conf(self, value): 
        if value > 1.0: 
            raise ValidationError('Invalid confidence')
        return value
    
    def validate_snapshot(self, value : str): 
        if value.name.endswith((".jpg", ".png", ".heic", ".heif")): 
            return value 
        else: 
            return ValidationError('Invalid snapshot')
    