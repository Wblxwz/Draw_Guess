from django.http import HttpResponse
from django.shortcuts import render
from . import models

def get_rooms_count(request):
    rooms = models.Room.objects.count()
    context = {'rooms_count': rooms}
    return render(request,'rooms/rooms.html',context)
