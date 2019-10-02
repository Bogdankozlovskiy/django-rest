from rest_framework import serializers
from .models import Visit
from django.contrib.auth.models import User


class UserSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class VisitSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('name_visit', 'date_of_visit', 'time_to_remind')
