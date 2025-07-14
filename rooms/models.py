from django.db import models

class Room(models.Model):
    rid = models.BigAutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_password = models.CharField(max_length=16)
    room_is_private = models.BooleanField()
    room_max_people = models.IntegerField()
    room_type = models.CharField(max_length=50)

class Message(models.Model):
    mid = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    uid = models.IntegerField()
