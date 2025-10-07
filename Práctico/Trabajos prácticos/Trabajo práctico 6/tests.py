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
    resultado = inscribirse(
        actividad="Tirolesa",
        horario="10:00",
        participantes=[{"nombre": "Toto", "edad": 10, "acepta_terminos": False}]
    )
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

def test_inscripcion_sin_cupos_disponibles():
    actividad = Actividad("Tirolesa", {"10:00": 5, "11:00": 0})
    resultado = inscribirse(actividad, "11:00", [{"nombre": "Toto", "acepta_terminos": True}])
    assert resultado["ok"] is False
    assert resultado["mensaje"] == "No hay cupos disponibles"

def test_no_indica_talle_en_vestimenta_requerida():
    actividad = Actividad("Palestra", {"10:00": 5, "11:00": 0})
    resultado = inscribirse(actividad, "10:00", [{"nombre": "Toto", "acepta_terminos": True}])
    assert resultado["ok"] is False
    assert resultado["mensaje"] == "Debe indicar el talle de la vestimenta requerida"
