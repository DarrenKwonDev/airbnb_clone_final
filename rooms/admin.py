from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price",)},
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
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    raw_id_fields = ("host",)

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
        "count_photos",
        "total_rating",
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
    def used_by(self, obj):
        return obj.rooms.count()

    list_display = ("name", "used_by")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
