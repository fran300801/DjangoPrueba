from django.core.management import BaseCommand
from datetime import date
from scrum.models import Tarea, Etiqueta, Programador


class Command(BaseCommand):
    help = "Este comando va a crear tareas de prueba"

    def handle(self, *args, **options):
        contador = 6
        try:
            programador = Programador(nombre=f"Francisco {contador}", apellido1 = f"Sobrino")
            programador.save()
            etiqueta = Etiqueta(nombre=f'Etiqueta de prueba {contador}')
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"Se ha guardado la etiqueta correctamente"))
            tarea = Tarea(nombre=f'Tarea de prueba {contador}', fecha_inicio=date.today(), programador=programador)
            tarea.save()
            tarea.etiqueta.add(etiqueta)
            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre {tarea.nombre} se ha insertado correctamente"))
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Se ha producido un fallo: {e}")
            )
