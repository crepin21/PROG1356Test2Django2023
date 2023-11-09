from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Capteur

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CapteurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capteur
        fields = ['nomUc', 'nomCapteur', 'temperature'] #Champs du model capteur