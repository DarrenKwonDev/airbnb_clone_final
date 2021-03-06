from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed


class Command(BaseCommand):

    help = "This command generated users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many do you want create User"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False,})
        seeder.execute()
        # 성공했다고 확인 메세지
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
