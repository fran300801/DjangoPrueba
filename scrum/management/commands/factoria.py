import random

from django.core.management import BaseCommand
from datetime import date
from faker import Faker
from scrum.models import Tarea, Sprint, Programador, Proyecto


class Command(BaseCommand):
    help = "Este comando va a ser una factoria"

    def handle(self, *args, **options):
        fake = Faker('es_ES')
        for i in range(10):
            programador = Programador(
                nombre=fake.first_name(),
                apellido1=fake.last_name()
            )
            programador.save()
        self.stdout.write(self.style.SUCCESS("Se han creado 10 programadores"))
        proyecto = Proyecto(nombre= 'Proyecto fumigación')
        proyecto.save()
        for i in range(4):
            sprint = Sprint(
                fecha_inicio=fake.date(),
                fecha_fin=fake.date(),
                proyecto=proyecto,
            )
            sprint.save()
        self.stdout.write(self.style.SUCCESS("Se han creado 4 sprints"))
        contador = 1
        programadores = Programador.objects.all()
        for i in range(30):
            sprint = Sprint.objects.all()
            tarea = Tarea(nombre=f'Tarea {contador}', fecha_inicio=fake.date(), fecha_fin=fake.date(), sprint=random.choice(sprint), programador=random.choice(programadores))
            tarea.save()
            contador+=1
        self.stdout.write(self.style.SUCCESS("Se han creado 30 tareas"))
