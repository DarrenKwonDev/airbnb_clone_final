from django.shortcuts import render
from . import models

# Create your views here.
def all_rooms(req):
    all_rooms = models.Room.objects.all()
    return render(req, "rooms/home.html", context={"rooms": all_rooms})
