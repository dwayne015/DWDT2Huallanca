from alumnos import alumno
import string

def informacionAlumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    nacionalidad = input("Ingrese la nacionalidad del alumno: ")

    return alumno(nombre, apellido, edad, 0, nacionalidad)

def registrar_alumnos():
    dataAlumnos = []
    while True:
        print("\nIngrese comando: (R: Registrar, C: Calificar, P: Promedio, S: Suma, X: Salir)")
        comando = input().upper()  #Validar las letras que esten en minusculas

        if comando == 'R':
            alumno = informacionAlumno()
            dataAlumnos.append(alumno)
            print("Alumno registrado con éxito.")

        elif comando == 'C':
            for alumno in dataAlumnos:
                while True:
                    try:
                        nota = int(input(f"Alumno {alumno.nombre} {alumno.apellido}, Ingrese nota: "))
                        if 0 <= nota <= 20:
                            alumno.registrarNota(nota)
                            break
                        else:
                            print("La nota debe estar en el rango de 0 a 20.")
                    except ValueError:
                        print("Error: Ingrese un número válido para la nota.")

        elif comando == 'P':
            cantidad_alumnos = len(dataAlumnos)
            total_notas = sum(alumno.leerNota() for alumno in dataAlumnos)
            promedio = total_notas / cantidad_alumnos if cantidad_alumnos > 0 else 0
            print(f"El promedio de notas para {cantidad_alumnos} alumnos es: {promedio:.2f}")

        elif comando == 'S':
            cantidad_alumnos = len(dataAlumnos)
            suma_notas = sum(alumno.leerNota() for alumno in dataAlumnos)
            print(f"La suma de notas de {cantidad_alumnos} alumnos es: {suma_notas}")

        elif comando == 'X':
            print("¡Hasta luego! Saliendo del programa.")
            break

        else:
            print("Comando inválido. Por favor, ingrese un comando válido.")

if __name__ == "__main__":
    print("Bienvenidos al registro de notas")
    registrar_alumnos()