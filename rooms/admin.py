from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Rule)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
