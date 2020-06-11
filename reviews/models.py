from django.db import models
from core import models as core_models


class Reviews(core_models.TimeStampedModel):

    """Reviews Model Def"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.review} - {self.room.name}"
