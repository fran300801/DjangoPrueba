from django.core.management import BaseCommand
from datetime import date
from scrum.models import Tarea, Etiqueta, Programador


class Command(BaseCommand):
    help = "Este comando va a crear tareas de prueba"

    def handle(self, *args, **options):
        programador = Programador.objects.get(pk=1)
        tarea = Tarea(nombre = 'Tarea con programador existente', programador = programador)
        tarea.save()
        self.stdout.write(self.style.SUCCESS(f"Se ha guardado la tarea {tarea} correctamente"))
