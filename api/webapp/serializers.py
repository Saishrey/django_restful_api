from dataclasses import fields
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        # fields = ('firstname', 'lastname') # to display specific fields
        fields = '__all__'
