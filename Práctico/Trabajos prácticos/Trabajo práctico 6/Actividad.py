class Actividad:
    def __init__(self, nombre, horarios):
        self.nombre = nombre
        self.horarios = horarios
        self.requiere_vestimenta = nombre in ["Palestra", "Escalada"]

    def tiene_cupos(self, horario):
        return self.horarios.get(horario, 0) > 0

    def inscribir_participante(self, horario):
        if self.tiene_cupos(horario):
            self.horarios[horario] -= 1
            return True
        return False