from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    city = str.capitalize(request.GET.get("city"))
    return render(request, "rooms/search.html", {"city": city})
