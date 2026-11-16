from scrum.models import Tarea, Sprint, Programador, Etiqueta

def validar_sprint_crear_tarea(tarea_json):
    sprint_id = tarea_json.get('sprint_id')

    if not sprint_id:
        return None

    try:
        return Sprint.objects.get(id=sprint_id).id
    except Sprint.DoesNotExist:
        raise ValueError('No existe un sprint con ese id')


def validar_programador_crear_tarea(tarea_json):
    programador_id = tarea_json.get('programador_id')
    if not programador_id:
        return None
    try:
        return Programador.objects.get(id=programador_id).id
    except Programador.DoesNotExist:
        raise ValueError('No existe un programador con ese id')