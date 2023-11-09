from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.models import Capteur
from quickstart.serializers import UserSerializer, GroupSerializer, CapteurSerializer
from django.http import QueryDict
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from django.http.response import JsonResponse 



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@api_view(['POST', 'GET'])
def enregistrement(request):
   if request.method == 'POST':
     # Suppression des valeurs contenues dans la base de données
      Capteur.objects.all().delete()
      print(request.POST)
      # Enregistrement des valeurs des objets de Capteur
      nameMicrocontoleur = request.POST["nomUc"]
      nameCapteur        = request.POST["nomCapteur"]
      tempMicrocontoleur = request.POST["temperature"]

     # humMicrocontroleur = request.POST["humidite"]
      
      data = Capteur()
      data.nomUc = nameMicrocontoleur
      data.nomCapteur = nameCapteur
      data.temperature = tempMicrocontoleur
      data.save()  # Sauvegarde dans la BD
      return HttpResponse('<h1>Post Request !</h1>')  # Message de confirmation
   elif request.method == 'GET':
      data = Capteur.objects.all()
      
      dataJson = CapteurSerializer(data, many=True)
      return JsonResponse(dataJson.data, safe=False)
   else:
      return HttpResponse('<h1>Invalid Request</h1>')  # Réponse par défaut pour les autres méthodes HTTP
class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Capteur.objects.all()
    serializer_class = CapteurSerializer