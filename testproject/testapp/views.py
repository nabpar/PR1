from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Student,Teacher
from testapp.serializer import StudentSerializer,TeacherSerializer
# Create your views here.


class ViewCURD(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class TeacherCURD(ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class= TeacherSerializer
    
    