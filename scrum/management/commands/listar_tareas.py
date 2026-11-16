from django.core.management import BaseCommand

from scrum.models import Tarea


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        tareas = Tarea.objects.all()

        for tarea in tareas:
            print(f"{tarea.id} {tarea.nombre}")

        self.stdout.write(self.style.SUCCESS(f"Este comando lista todas las tareas"))