from django.shortcuts import render
from . import models
import random
from django.http import JsonResponse
from myapp.serializer import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse


def displayhtml(request):
        student_name=["hari","giri","ram","krishna","geetha"]
        for user in student_name:
            db = models.Student(
            Name=user,
            Marks=random.randint(50,100))
            db.save()
        data=models.Student.objects.values()
        context_data={'data':data}
        return render(request,'student.html',context=context_data)


@api_view(['GET'])
def displayjson(request):
    if request.method == 'GET':
        data = models.Student.objects.values()
        serialized = Serializer(data, many=True)
        return Response(serialized.data)

@api_view(['GET'])
def student_detail(request, pk):
    if request.method == 'GET':
        data = models.Student.objects.get(id=pk)
        serialized = Serializer(data)
        return Response(serialized.data)
