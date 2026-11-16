from django.test import TestCase
from .models import *
from datetime import date

# Create your tests here.

class TareaTest(TestCase):

    def setUp(self):
        self.programador = Programador.objects.create(nombre = "Francisco")
        self.sprint = Sprint.objects.create(fecha_inicio = date(2026, 11, 9), fecha_fin = date(2026, 11, 9))

    def test_numero_sprint(self):
        sprint = Sprint.objects.count()
        self.assertEqual(sprint, 1)

    # Aquí te lo cuenta como 2 sprints porque pilla el de setUp y este
    def test_crear_sprint(self):
        self.sprint = Sprint.objects.create(fecha_inicio = date(2026, 11, 9), fecha_fin = date(2026, 11, 9))
        sprint = Sprint.objects.count()
        self.assertEqual(sprint, 2)

    def test_suma(self):
        resultado = 4 + 4
        self.assertEqual(resultado, 8)

    def test_resta(self):
        resultado = 10 - 5
        self.assertEqual(resultado, 5)

    def test_comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"

        if nombre.strip().lower() != nombre2.strip().lower():
            comprobacion = False

        self.assertTrue(comprobacion)

    def test_crear_tarea_api(self):
        datos = {
            "nombre": "Francisco",
            "fecha_inicio": date(2026, 11, 9),
            "fecha_fin": date(2026, 11, 9),
            "completa": False,
            "sprint_id": self.sprint.id,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
        "/api/crear_tarea/",
        data=datos,
        content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(Tarea.objects.count(), 1)