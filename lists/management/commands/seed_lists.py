import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from reviews import models as review_models
from users import models as user_models
from rooms import models as rooms_models
from lists import models as lists_models
from django_seed import Seed


class Command(BaseCommand):

    help = "This command generated lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many do you want create lists"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder.add_entity(
            lists_models.List,
            number,
            {
                # user 이름으로 users 중 하나를 choice합니다.
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = lists_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        # 성공했다고 확인 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
