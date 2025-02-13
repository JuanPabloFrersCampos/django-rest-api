from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET', 'POST'])
def collection_request(request):
    if request.method == 'GET':
      users = User.objects.all()
      serializer = UserSerializer(users, many=True)
      return Response(serializer.data)

    elif request.method == 'POST':
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def entity_request(request, id):
  try:
    user = User.objects.get(pk=id)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = UserSerializer(user).data
    return Response(serializer)
  
  elif request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
