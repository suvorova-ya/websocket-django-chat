from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import  Room, Message

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RoomSerializer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

def index(request):
    return render(request, 'chat/index.html')

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@login_required
def room_create(request):
    
    if request.method == "GET":
        return render(request, 'chat/room_create.html')
    
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
@login_required
def room_delete(request, slug):
    room = Room.objects.get(slug=slug)
    room_name = room.name
    if request.method == "GET":
        return render(request, 'chat/room_delete.html', {"room_name": room_name})

    if request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'PATCH'])
@parser_classes([JSONParser])
@login_required
def room_edit(request, slug):
    room_name = Room.objects.get(slug=slug).name
    if request.method == 'GET':
        return render(request, 'chat/room_edit.html', {"room_name": room_name})
    
    elif request.method == 'PATCH':
        room = Room.objects.get(slug=slug)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ListRoom(ListView):
    model = Room
    template_name = 'chat/room_list.html'
    context_object_name = 'room'
   

