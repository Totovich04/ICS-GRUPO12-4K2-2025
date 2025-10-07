
def inscribirse(actividad, horario, participantes):
    # Verificar que todos los participantes acepten los términos y condiciones
    for participante in participantes:
        if not participante.get("acepta_terminos", False):
            return {"ok": False, "mensaje": "Debe aceptar los términos y condiciones"}
    return {"ok": True, "mensaje": "Inscripción exitosa"}