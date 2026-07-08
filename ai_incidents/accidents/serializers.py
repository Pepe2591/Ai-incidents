from rest_framework.serializers import ModelSerializer 
from .models import Camera, Dangerous_event

class CameraModelSerializer(ModelSerializer): 
    class Meta:
        model = Camera 
        fields = '__all__'

class FiresModelSerializer(ModelSerializer): 
    class Meta: 
        model = Dangerous_event
        fields = '__all__' 

class CollapseModelSerializer(ModelSerializer): 
    class Meta: 
        model = Dangerous_event
        fields = '__all__' 

class ExplosionsModelSerializer(ModelSerializer): 
    class Meta: 
        model = Dangerous_event
        fields = '__all__' 

class AnalysisModelSerializer(): 
    class Meta: 
        model = Dangerous_event
        fiels = '__all__'

class LogsModelSerializer(ModelSerializer): 
    class Meta: 
        model = Dangerous_event
        fields = '__all__' 

class CoreServiceSerializer(ModelSerializer): 
    class Meta: 
        model = Dangerous_event
        fileds = '__all__'
    