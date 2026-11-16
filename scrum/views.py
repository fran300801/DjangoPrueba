import json
from json import JSONDecodeError

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from scrum.management.commands import validaciones
from scrum.models import Tarea, Sprint, Programador, Etiqueta


# Create your views here.

def bienvenida(request):
    return HttpResponse("Hola chicos e Inmaculada estamos en nuestro primer controlador")


def listarTareas(request):
    if request.method != "GET":
        return JsonResponse("Error: está petición solo funciona con GET")


    tareas = Tarea.objects.all().values()

    return JsonResponse(list(tareas), safe=False)

def listarTareasID(request, id):
    if request.method != "GET":
        return JsonResponse("Error: esta petición solo funciona con GET")

    tarea = Tarea.objects.get(id=id)

    datos = {
        "id": tarea.id,
        "nombre": tarea.nombre,
        "fecha_inicio": (
            tarea.fecha_inicio.isoformat()
            if tarea.fecha_inicio else None
        ),
        "fecha_fin": (
            tarea.fecha_fin.isoformat()
            if tarea.fecha_fin else None
        ),
        "completa": tarea.completa,
        "sprint": tarea.sprint,
        "programador": tarea.programador,
    }

    return JsonResponse(datos)

def listarTareaMejorado(request, id):
    if request.method != "GET":
        return JsonResponse("Error: esta petición solo funciona con GET")

    tarea = Tarea.objects.filter(id=id).values().first()

    return JsonResponse(tarea)

def listarTareaCompletada(request):
    if request.method != "GET":
        return JsonResponse("Error: esta petición solo funciona con GET")

    tarea = Tarea.objects.filter(completa=True).values()

    return JsonResponse(list(tarea), safe=False)

@csrf_exempt
def crear_tarea(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Tipo de petición no es correcta'}, status=405)

    try:
        tarea_json = json.loads(request.body)
    except JSONDecodeError:
        return JsonResponse({'error': 'El Json no está bien formado'}, status=400)


    # Si en la tarea vienen etiquetas y esas etiquetas no existen, quiero que las guardes

    try:


        # etiqueta = obtener_o_crear_etiqueta(tarea_json)
        tarea = Tarea.objects.create(
            nombre = tarea_json.get("nombre"),
            fecha_inicio = tarea_json.get("fecha_inicio"),
            fecha_fin = tarea_json.get("fecha_fin"),
            completa = tarea_json.get("completa", False),
            sprint_id = validaciones.validar_sprint_crear_tarea(tarea_json),
            programador_id = validaciones.validar_programador_crear_tarea(tarea_json),
        )
        etiquetas = tarea_json.get("etiquetas", [])
        crear_etiqueta(etiquetas, tarea)

        for etiqueta in etiquetas:
            etiqueta_model,creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
            tarea.etiqueta.add(etiqueta_model)
            if not creada:
                print("Se ha creado la etiqueta")
            else:
                print("No se ha creado la etiqueta")
        return JsonResponse({
            'exito': 'Se ha creado correctamente la tarea',
            'tarea_id': tarea.id
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def crear_etiqueta(etiquetas, objeto):
    for etiqueta in etiquetas:
        etiqueta_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
        objeto.etiqueta.add(etiqueta_model)
        if not creada:
            print("Se ha creado la etiqueta")
        else:
            print("No se ha creado la etiqueta")

@csrf_exempt
def crear_programador(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Tipo de petición no es correcta'},status=405)
    try:
        programador_json = json.loads(request.body)
    except JSONDecodeError as e:
        return JsonResponse({'error': 'El Json no esta bien formado'},status=400)

    programador = Programador.objects.create(
        nombre = programador_json.get("nombre"),
        apellido1 = programador_json.get("apellido1")
    )
    etiquetas = programador_json.get("etiquetas", [])
    crear_etiqueta(etiquetas, programador)

    return JsonResponse({'exito': 'Se ha creado correctamente el programador',
                         'tarea': programador.id})