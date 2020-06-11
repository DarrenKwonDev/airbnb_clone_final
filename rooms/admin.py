from django.contrib import admin

from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price",)},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("amenities", "facilities", "rules",)},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    def count_amenities(self, obj):
        print(obj.amenities.count())
        return obj.amenities.count()

    count_amenities.short_description = "amenities"

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "rules",
        "country",
    )

    search_fields = ["^city", "host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "rules",
    )

    ordering = ("name", "price", "bedrooms")


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Rule)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
