import matplotlib.pyplot as plt
import numpy as np

cont = 0 # Contador
Estudiantes = {} #Diccionario de Estudiantes
Nmat = 0 # Cant Materias
Materias = {} #Diccionario de Materias

promMat = {}
reprobados_por_materia = {}
proMaxMat = 0
proMinMat = 0
promMat=0
# Ingresa la cantidad de estudiantes
Nest = int(input("Ingrese la cantidad de estudiantes a registrar: "))
# Ingresa la cantidad de materias
Nmat = int(input("Ingrese la cantidad de materias a registrar: "))

# Ingresar datos de los estudiantes
def estudiante(Estudiantes=Estudiantes, cont=cont, Nest=Nest):
    while cont < Nest:
        cestud = int(input("Ingrese la cédula del estudiante: "))
        if cestud not in Estudiantes:
            estud = input("Ingrese los nombres completos del estudiante: ")
            Estudiantes[cestud] = {'nombre': estud, 'calificaciones': {}, 'promedio': 0, 'Estado': ''}# Investigar
            cont += 1
        else:
            print("La cédula ya está en uso. Por favor, ingrese una cédula única.")

# Ingresar datos de las materias
def materias(cont2=cont):
    cont2=0
    while cont2 < Nmat:
        codmat = input("Ingrese el codigo de la materia (Ejemplo: A-1): ")
        if codmat not in Materias:
            materia = input("Ingrese el nombre de la materia: ")
            #If para vaildar que la materia y el codigo coincidan -----------------------------------
            Materias[codmat] = {'materia':materia, 'numReprobados': 0, 'promMat': 0}
            cont2 += 1
        else:
            print("El codigo ya está en uso. Por favor, ingrese una codigo único.")
    return sorted(Materias.values())# Investigar///

# Agregar calificaciones
def calificaciones(Estudiantes=Estudiantes, Materias=Materias):
    for cedula in Estudiantes:
        for materia in Materias:
            while True: #Investigar///
                print(f"Calificacion del estudiante {Estudiantes[cedula]['nombre']} en la materia {Materias[materia]['materia']}: ")
                calificacion = float(input())
                if 0 <= calificacion <= 100:
                    Estudiantes[cedula]['calificaciones'][Materias[materia]['materia']] = calificacion
                    break
                else:
                    print("Calificación fuera del rango 0 a 100. Por favor, ingrese nuevamente.")

# Promedio de cada materia
def promedioMaterias():
    global promMat, proMaxMat, proMinMat
    for materia in Materias:
        suma = 0
        for cedula in Estudiantes:
            suma += Estudiantes[cedula]['calificaciones'][materia]
        Materias[materia]['promMat']= suma / len(Estudiantes)
    
    # Usar for e if clacular el promedio Mayor y el menor -----------------------------------------------------------
    proMaxMat = max(Materias['promMat'])
    proMinMat = min(Materias['promMat'])

# Promedio de cada estudiante
def promedioEstudiante():
    global proMaxMat, proMinMat
    for cedula in Estudiantes:
        suma = 0
        for materia in Materias:
            suma += Estudiantes[cedula]['calificaciones'][materia]
        promEst = suma / Nmat
        Estudiantes[cedula]['promedio'] = promEst
        # if para ver cual estudiante tiene promedio mayor o menor---------------------------------------------------


        
# Estado de cada estudiante (Aprobado o Reprobado)
def calcular_reprobados():
    for materia in Materias:
        for cedula in Estudiantes:
            if Estudiantes[cedula]['calificaciones'][materia] < 70:
                Materias[materia]['numReprobados'] += 1


# Investigar funcionabilidad, en especial con la funcion de calificaciones
def ingresar_nuevo_estudiante():
    global cont, Nest
    Nest += 1
    estudiante()
    calificaciones()

# Revisar!!!!!!!
def editar_informacion_estudiante(Estudiantes=Estudiantes):
    cestud = int(input("Ingrese la cédula del estudiante a editar: "))
    if cestud in Estudiantes:
        estud = input("Ingrese los nuevos nombres completos del estudiante: ")
        Estudiantes[cestud]['nombre'] = estud
        print("Información del estudiante editada correctamente.")
        editar_notas = input("¿Desea editar las calificaciones del estudiante? (s/n): ")
        if editar_notas.lower() == 's':
            calificaciones({cestud: Estudiantes[cestud]})
        else:
            print("Calificaciones no editadas.")
    else:
        print("La cédula ingresada no existe.")


#Revisar!!!!!!!!
def tabla():
    global Estudiantes, Materias
    tabla = np.zeros((len(Estudiantes) + 1, len(Materias) + 1))
    tabla[0, 0] = "Estudiantes/Materias"
    for i in range(1, len(Materias) + 1):
        tabla[0, i] = Materias[i]['materia']
    for j in range(1, len(Estudiantes) + 1):
        tabla[j, 0] = Estudiantes[j]['nombre']
        for k in range(1, len(Materias) + 1):
            tabla[j, k] = Estudiantes[j]['calificaciones'][k]
    print(tabla)

#Revisar!!!!!!!!!!
def graficas():
    global reprobados_ordenados
    print("\nOpciones:")
    print("1. Estudiantes reprobados por materia")
    print("2. Promedio de calificaciones por materia")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        plt.bar(Materias.keys(), Materias['numReprobados'])
        plt.xlabel("Materia")
        plt.ylabel("Cantidad de estudiantes reprobados")
        plt.title("Estudiantes reprobados por materia")
        plt.show()
    elif opcion == 2:
        plt.bar(promMat.keys(), promMat.values())
        plt.xlabel("Materia")
        plt.ylabel("Promedio de calificaciones")
        plt.title("Promedio de calificaciones por materia")
        plt.show()
    elif opcion == 3:
        pass
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")

# Llamar a las funciones
estudiante()
materias()
calificaciones()
promedioMaterias()
promedioEstudiante()

# Opciones adicionales Revisar!!!!!!!!!!!!!!!!!!!!
while True:
    print("\nOpciones adicionales:")
    print("1. Ingresar un nuevo estudiante")
    print("2. Editar la información de un estudiante")
    print("3. Tabla de notas")
    print("4. Graficar")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        ingresar_nuevo_estudiante()
    elif opcion == 2:
        editar_informacion_estudiante()
    elif opcion == 3:
        tabla()
    elif opcion == 4:
        graficas()
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")