from rest_framework import serializers
from myapp.models import Students

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'