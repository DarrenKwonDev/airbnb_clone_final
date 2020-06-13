import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from datetime import datetime, timedelta
from users import models as user_models
from rooms import models as rooms_models
from reservations import models as reservations_models
from django_seed import Seed


class Command(BaseCommand):

    help = "This command generated reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many do you want create reservations",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(
            reservations_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()

        # 성공했다고 확인 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
