from django.shortcuts import render
from .serializers import StudentSerializer
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin, UpdateModelMixin , DestroyModelMixin 


# Create your views here.

class studentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request, *args,**kwargs):
        return self.list(request, *args,**kwargs)
      
      
class studentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self,request, *args,**kwargs):
        return self.create(request, *args,**kwargs)
      
      
class studentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request, *args,**kwargs):
        return self.retrieve(request, *args,**kwargs)
      
      
      
class studentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self,request, *args,**kwargs):
        return self.update(request, *args,**kwargs)
      
      
class studentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def delete(self,request, *args,**kwargs):
        return self.destroy(request, *args,**kwargs)
      
      
class LCStudentapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request, *args,**kwargs):
        return self.list(request, *args,**kwargs)
      
    def post(self,request, *args,**kwargs):
        return self.create(request, *args,**kwargs)
      
      
      
class RUDStudentapi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request, *args,**kwargs):
        return self.retrieve(request, *args,**kwargs)
      
    
    def put(self,request, *args,**kwargs):
        return self.update(request, *args,**kwargs)
      
    
    def delete(self,request, *args,**kwargs):
        return self.destroy(request, *args,**kwargs)
      

  
