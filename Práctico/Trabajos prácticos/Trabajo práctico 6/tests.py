import pytest
from ecoPark import inscribirse
from actividad import Actividad

# def test_acepta_terminos_y_condiciones():
#    resultado = inscribirse(
#        actividad = "Tirolesa", 
#        horario = "10:00",
#        participantes = [{"nombre": "Toto", "edad": 10, "acepta_terminos": True}]
#    )
#    assert resultado["ok"] is True
#    assert resultado["mensaje"] == "Inscripción exitosa"

def test_no_acepta_terminos_y_condiciones():
    actividad = Actividad("Tirolesa")
    actividad.agregar_disponibilidad("2025-10-10", {"10:00": 5, "11:00": 0})
    resultado = inscribirse(actividad, "2025-10-10", "11:00", [{"nombre": "Toto", "acepta_terminos": False}])
    assert resultado["ok"] is False
    assert resultado["mensaje"] == "Debe aceptar los términos y condiciones"

# def test_inscripcion_con_cupos_disponibles():
#    resultado = inscribirse(
#        actividad="Tirolesa",
#        horario="10:00",
#        participantes=[{"nombre": "Toto", "edad": 10, "acepta_terminos": True}]
#    )
#    assert resultado["ok"] is True
#    assert resultado["mensaje"] == "Inscripción exitosa"

def test_sin_cupos_para_fecha_horario():
    actividad = Actividad("Tirolesa")
    actividad.agregar_disponibilidad("2025-10-10", {"10:00": 0})
    resultado = inscribirse(
        actividad,
        "2025-10-10",
        "10:00",
        [{"nombre": "Toto", "acepta_terminos": True}]
    )
    assert resultado["ok"] is False
    assert resultado["mensaje"] == "No hay cupos disponibles"

def test_no_indica_talle_en_vestimenta_requerida():
    actividad = Actividad("Palestra")
    actividad.agregar_disponibilidad("2025-10-10", {"10:00": 5})
    resultado = inscribirse(actividad, "2025-10-10", "10:00", [{"nombre": "Toto", "acepta_terminos": True}])
    assert resultado["ok"] is False
    assert resultado["mensaje"] == "Debe indicar el talle de la vestimenta requerida"

#TODO test horario no disponible (falla)
#TODO test Probar inscribirse a una actividad sin ingresar talle de vestimenta porque la actividad no lo requiere (pasa)
#TODO test que pasa
#TODO(opcional) front