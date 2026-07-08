from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response 
from .models import Camera, Dangerous_event
from .serializers import (CameraModelSerializer, FiresModelSerializer, CollapseModelSerializer, 
                          ExplosionsModelSerializer, CoreServiceSerializer, AnalysisModelSerializer, LogsModelSerializer) 

# Create your views here.

class CameraModelViewSet(viewsets.ModelViewSet): 
    queryset = Camera.objects.all()
    serializer_class = CameraModelSerializer

class FiresModelViewSet(viewsets.ModelViewSet): 
    queryset = Dangerous_event.objects.all()
    serializer_class = FiresModelSerializer 

class CollapseMidelViewSet(viewsets.ModelViewSet): 
    queryset = Dangerous_event.objects.all() 
    serializer_class = CollapseModelSerializer

class ExplosionModelViewSet(viewsets.ModelViewSet): 
    queryset = Dangerous_event.objects.all() 
    serializer_class = ExplosionsModelSerializer

class CoreSericeViewSet(viewsets.ViewSet): 
    def list(self, request): 
        queryset = Dangerous_event.objects.all()
        serializer = CoreServiceSerializer(queryset)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Dangerous_event.objects.all()
        coreService = get_object_or_404(queryset, pk = pk)
        serializer = CoreServiceSerializer(coreService)
        return Response(serializer.data) 
                

class LogsViewSet(viewsets.ViewSet): 
    def list(self, request): 
        queryset = Dangerous_event.objects.all()
        serializer = LogsModelSerializer(queryset) 
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None): 
        queryset = Dangerous_event.objects.all() 
        logs = get_object_or_404(queryset, pk = pk)
        serializer = LogsModelSerializer(logs)
        return Response(serializer.data)
    
    def destroy(self, request, pk = None): 
        queryset = Dangerous_event.objects.all() 
        log_obj = get_object_or_404(queryset, pk = pk)
        log_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

class AnalysisViewSet(viewsets.ViewSet): 
    def list(self, request): 
        queryset = Dangerous_event.objects.all()
        serializer = AnalysisModelSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None): 
        queryset = Dangerous_event.objects.all()
        analysis = get_object_or_404(queryset, pk = pk)
        serialiser = AnalysisModelSerializer(analysis)
        return Response(serialiser.data)

