from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Student
from testapp.serializer import StudentSerializer
# Create your views here.


class ViewCURD(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    
    