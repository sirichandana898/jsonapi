from django.shortcuts import render
from . import models,forms
import random
from django.http import JsonResponse
from myapp.serializer import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render,redirect
from rest_framework.parsers import JSONParser
from rest_framework import status


def student_create(request):
    if request.method == 'GET':
        form = forms.Studentform()
        context_data = {
            'heading': 'Student details',
            'title': 'Student details',
            'form': form
        }
        return render(request, 'studentform.html', context=context_data)
    else:
        form = forms.Studentform(request.POST)
        if form.is_valid():
            db = models.Students(
                Name=form.cleaned_data['Name'],
                Marks=form.cleaned_data['Marks'],
            )
            db.save()
        return redirect('display/html')


def student_update(request, id):
    if request.method == 'GET':
        students = models.Students.objects.filter(id=id).values()
        form = forms.Studentform(students[0])
        context_data = {
            'title': 'Update student details',
            'heading': 'Update student details',
            'form': form
        }
        return render(request, 'studentform.html', context=context_data)
    else:
        form = forms.Studentform(request.POST)
        if form.is_valid():
            db = models.Students.objects.filter(id=id)
            db.update(
                Name=form.cleaned_data['Name'],
                Marks=form.cleaned_data['Marks'],
            )
        return redirect('/display/html')


def student_delete(request, id):
    models.Students.objects.filter(id=id).delete()
    return redirect('/display/html')


@api_view(['GET'])
def display(request):
    students = models.Students.objects.values()
    context_data = {
        'header': list(students[0].keys()),
        'data': students,
        'title': 'Student list',
        'update': True,
        'delete': True,
    }
    if '/html' in request.get_full_path():
        return render(request, 'student.html', context=context_data)
    elif '/json' in request.get_full_path():
        if request.method == 'GET':
            serialized = Serializer(students, many=True)
            return Response(serialized.data)


def home(request):
    return render(request,'home.html')


@api_view(['PUT', 'DELETE'])
def student_detail(request, pk):
    student = models.Students.objects.get(pk=pk)
    if request.method == 'PUT':
        student_data = JSONParser().parse(request)
        serialized = Serializer(student, data=student_data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student entry deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def student_list(request):
    if request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = Serializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)