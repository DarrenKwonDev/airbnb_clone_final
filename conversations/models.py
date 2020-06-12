from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    class Meta:
        verbose_name_plural = "Conversations"

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        print(usernames)
        return ", ".join(usernames)

    def count_messages(self):
        return self.message.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):
    messages = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="message", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="message", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.conversation}"
