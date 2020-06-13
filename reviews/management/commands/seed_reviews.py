import random
from django.core.management.base import BaseCommand
from reviews import models as review_models
from users import models as user_models
from rooms import models as rooms_moels
from django_seed import Seed


class Command(BaseCommand):

    help = "This command generated reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many do you want create room"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # 모든 유저를 가져옵니다.
        users = user_models.User.objects.all()
        # 모든 방을 가져옵니다.
        rooms = rooms_moels.Room.objects.all()
        seeder.add_entity(
            review_models.Reviews,
            number,
            {
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                # user 이름으로 users 중 하나를 choice합니다.
                "user": lambda x: random.choice(users),
                # room 이름으로 rooms 중 하나를 choice합니다.
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()

        # 성공했다고 확인 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
