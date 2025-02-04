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


#Check UwU
def tabla():
    global Estudiantes, Materias
    
    # Ordenar estudiantes por nombre
    estudiantes_ordenados = sorted(Estudiantes.items(), key=lambda item: item[1]['nombre'])
    estudiantes_ordenados = {key: value for key, value in estudiantes_ordenados}
    
    # Ordenar materias por nombre
    materias_ordenadas = sorted(Materias.items(), key=lambda item: item[1]['materia'])
    materias_ordenadas = {key: value for key, value in materias_ordenadas}
    
    # Crear tabla vacía
    tabla = np.empty((len(estudiantes_ordenados) + 1, len(materias_ordenadas) + 1), dtype=object)
    tabla[0, 0] = "Estudiantes/Materias"
    
    # Llenar encabezados de materias
    i = 1
    for codmat, materia in materias_ordenadas.items():
        tabla[0, i] = materia['materia']
        i += 1
    
    # Llenar filas de estudiantes y sus calificaciones
    j = 1
    for cedula, estudiante in estudiantes_ordenados.items():
        tabla[j, 0] = estudiante['nombre']
        k = 1
        for codmat, materia in materias_ordenadas.items():
            tabla[j, k] = estudiante['calificaciones'].get(materia['materia'], 'N/A')
            k += 1
        j += 1

    print(tabla)

#Revisar!!!!!!!!!!
def graficas():
    global reprobados_ordenados
    print("\nOpciones:")
    print("1. Promedios de Las materias")
    print("2. Numero de estudiantes reprobados por materia")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        plt.bar(Materias['materia'], Materias['promMat'])
        plt.xlabel("Materias")
        plt.ylabel("Promedio General")
        plt.title("Promedios de mAterias")
        plt.show()
    elif opcion == 2:
        plt.bar(Materias['materia'], Materias['numReprobados'])
        plt.xlabel("Materias")
        plt.ylabel("Estudiantes reprobados")
        plt.title("N.Estudiantes Reprobados")
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