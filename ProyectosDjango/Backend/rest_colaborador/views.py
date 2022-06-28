from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Colaborador
from .serializers import ColaboradorSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_colaboradores(request):
    #Esta función o método devuelve o muestra todos los vehiculos en formato Json
    if request.method =='GET':
        colaborador = Colaborador.objects.all()
        serializer = ColaboradorSerializer(colaborador, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer=ColaboradorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201.CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
