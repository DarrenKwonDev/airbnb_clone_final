from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_countries import countries
from . import models


class HomeView(ListView):

    model = models.Room

    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    model = models.Room


def search(request):

    # 유저가 입력한 값을 url에서 가져옴 why? 입력한 후에도 value로 남겨주려고
    city = str.capitalize(request.GET.get("city", "Anywhere"))
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    instant = bool(request.GET.get("instant", False))
    super_host = bool(request.GET.get("super_host", False))

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    # 유저가 select 할 수 있도록 정보를 가져옴

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["guests__gte"] = bedrooms

    if beds != 0:
        filter_args["guests__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if super_host is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
