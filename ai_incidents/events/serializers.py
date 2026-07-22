from rest_framework.serializers import ModelSerializer, ValidationError
from django.shortcuts import get_object_or_404
from .models import Camera, Event
from .validators import EventsModelSerializer 


class CameraModelSerializer(ModelSerializer): 
    class Meta:
        model = Camera 
        fields = '__all__'

    def validate_owner(self, value): 
        pass
    
    def validate_id(self, value : int): 
        if not self.Meta.model.objects.filter(id = value).exists(): 
            raise ValidationError('Camera not found')
        
    def validate_name(self, value : str): 
        if value.strip() == '': 
            raise ValidationError('Name is required')
        return value
    

class Accident(EventsModelSerializer):
    def validate_event_types(self, value): 
        if not self.Meta.model.objects.filter()



class FiresModelSerializer(EventsModelSerializer): 

    def validate_categorys(self, value : list[Event]): 
        allowed_events = ['fires', 'smoke']
        if all(category for category in value if category.name in allowed_events): 
            return value 
        else: 
            raise ValidationError('Invalid event type')


class CollapseModelSerializer(EventsModelSerializer): 

    def validate_categorys(self, value : list[Event]): 
        allowed_events = ['collapse']
        if all(category for category in value if category.name in allowed_events): 
            return value 
        else: 
            raise ValidationError('Invalid event type')

class ExplosionsModelSerializer(EventsModelSerializer): 

    def validate_categorys(self, value : list[Event]): 
        allowed_events = ['explosions']
        if all(category for category in value if category.name in allowed_events): 
            return value 
        else: 
            raise ValidationError('Invalid event type')

class AnalysisModelSerializer(): 
    class Meta: 
        model = Event
        fiels = '__all__'

class LogsModelSerializer(ModelSerializer): 
    class Meta: 
        model = Event
        fields = '__all__' 

class CoreServiceSerializer(ModelSerializer): 
    class Meta: 
        model = Event
        fileds = '__all__'
    