from actividad import Actividad

def inscribirse(actividad, horario, participantes):
    # Verificar que todos los participantes acepten los términos y condiciones
    for participante in participantes:
        if not acepta_terminos(participante):
            return {"ok": False, "mensaje": "Debe aceptar los términos y condiciones"}

    # Verificar si hay cupos disponibles
    if not actividad.tiene_cupos(horario):
        return {"ok": False, "mensaje": "No hay cupos disponibles"}
    
    if actividad.requiere_vestimenta:
        for participante in participantes:
            if "talle_vestimenta" not in participante:
                return {"ok": False, "mensaje": "Debe indicar el talle de la vestimenta requerida"}

    return {"ok": True, "mensaje": "Inscripción exitosa"}

def acepta_terminos(participante):
    return participante.get("acepta_terminos", False)


