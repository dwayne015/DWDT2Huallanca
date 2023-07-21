import string

class alumno:
    def __init__(self,nombre,apellido,edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nac = nacionalidad

    def leerNota(self):
        return self.nota

    def registrarNota(self, notaAlumno):
        if notaAlumno >= 0 and notaAlumno <= 20:
            self.nota = notaAlumno
            return True
        else:
            print("La nota debe estar en el rango de 0 a 20.")
            return False


