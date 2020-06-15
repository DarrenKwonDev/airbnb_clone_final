from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
def all_rooms(request):
    page = int(request.GET.get("page"))
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, per_page=10,)
    rooms = paginator.get_page(page)

    print(vars(rooms))
    print(vars(rooms.paginator))

    return render(request, "rooms/home.html", {"rooms": rooms},)
