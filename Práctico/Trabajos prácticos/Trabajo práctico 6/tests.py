import pytest
from ecoPark import inscribirse
def test_acepta_terminos_y_condiciones():
    resultado = inscribirse(
        actividad = "Tirolesa", 
        horario = "10:00",
        participantes = [{"nombre": "Toto", "edad": 10, "acepta_terminos": True}]
    )
    assert resultado["ok"] is True
    assert resultado["mensaje"] == "Inscripción exitosa"

