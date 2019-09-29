from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Visit


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#class VisitSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Visit
#        fields = ['name_visit', 'date_of_visit', 'time_to_remind']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('name_visit', 'date_of_visit', 'time_to_remind')
