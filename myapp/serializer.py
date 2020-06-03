from rest_framework import serializers
from myapp.models import Student

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'