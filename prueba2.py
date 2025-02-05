import matplotlib.pyplot as plt
import numpy as np

cont = 0 # Contador
Estudiantes = {} #Diccionario de Estudiantes
Nmat = 0 # Cant Materias
Materias = {} #Diccionario de Materias
tamText = 0
# Ingresa la cantidad de estudiantes
Nest = int(input("Ingrese la cantidad de estudiantes a registrar: "))
# Ingresa la cantidad de materias
Nmat = int(input("Ingrese la cantidad de materias a registrar: "))

# Ingresar datos de los estudiantes
def estudiante(Estudiantes=Estudiantes, cont=cont, Nest=Nest, tamText=tamText):
    while cont < Nest:
        cestud = input("Ingrese la cédula del estudiante: ")
        if cestud not in Estudiantes and len(cestud) == 10:
            while True:
                estud = input("Ingrese los nombres completos del estudiante: ")
                if estud.count(" ") == 3:
                    Estudiantes[cestud] = {'nombre': estud, 'calificaciones': {}, 'promedio': 0, 'Estado': ''}
                    cont += 1
                    if len(estud) > tamText:
                        tamText = len(estud)
                    break
                else:
                    print("Nombre no valido")
        else:
            print("La cédula ya está en uso o no tiene 10 dígitos. Por favor, ingrese una cédula válida.")

# Ingresar datos de las materias
def materias(cont2=cont):
    cont2 = 0
    while cont2 < Nmat:
        codmat = input("Ingrese el codigo de la materia (Ejemplo: A-1): ")
        materia = input("Ingrese el nombre de la materia: ")

        if codmat not in Materias and codmat[0] == materia[0]:
            Materias[codmat] = {'materia': materia, 'numReprobados': 0, 'promMat': 0}
            cont2 += 1
        else:
            print("Los datos no coinciden o el código ya está en uso. Por favor, ingrese de nuevo los datos.")

# Agregar calificaciones
def calificaciones(Estudiantes=Estudiantes, Materias=Materias):
    for cedula in Estudiantes:
        for materia in Materias:
            while True:
                print(f"Calificacion del estudiante {Estudiantes[cedula]['nombre']} en la materia {Materias[materia]['materia']}: ")
                calificacion = float(input())
                if 0 <= calificacion <= 100:
                    Estudiantes[cedula]['calificaciones'][Materias[materia]['materia']] = calificacion
                    break
                else:
                    print("Calificación fuera del rango 0 a 100. Por favor, ingrese nuevamente.")

# Promedio de cada materia
def promedioMaterias():
    global proMaxMat, proMinMat
    proMaxMat = -1  
    proMinMat = 101 
    for materia in Materias:
        suma = 0
        for cedula in Estudiantes:
            suma += Estudiantes[cedula]['calificaciones'][Materias[materia]['materia']]
        Materias[materia]['promMat'] = suma / len(Estudiantes)

        if Materias[materia]['promMat'] > proMaxMat:
            proMaxMat = Materias[materia]['promMat']
        if Materias[materia]['promMat'] < proMinMat:
            proMinMat = Materias[materia]['promMat']

#Promedio De cada estudiante
def promedioEstudiante():
    global estMax, estMin, proMaxEst, proMinEst
    proMaxEst = -1
    proMinEst = 101
    for cedula in Estudiantes:
        suma = 0
        for materia in Materias:
            suma += Estudiantes[cedula]['calificaciones'][Materias[materia]['materia']]
        promEst = suma / Nmat
        Estudiantes[cedula]['promedio'] = promEst
        if promEst > proMaxEst:
            proMaxEst = promEst
            estMax = Estudiantes[cedula]['nombre']
        if promEst < proMinEst:
            proMinEst = promEst
            estMin = Estudiantes[cedula]['nombre']
        
# Estado de cada estudiante (Aprobado o Reprobado)
def calcular_reprobados():
    for materia in Materias:
        for cedula in Estudiantes:
            if Estudiantes[cedula]['calificaciones'][Materias[materia]['materia']] < 70:
                Materias[materia]['numReprobados'] += 1
                Estudiantes[cedula]['Estado'] = "Reprobado"
            else:
                Estudiantes[cedula]['Estado'] = "Aprobado"

# Ingresar Estudiante nuevo
def ingresar_nuevo_estudiante():
    global Nest
    Nest += 1
    estudiante()
    calificaciones()

# Revisar!!!!!!!
def editar_informacion_estudiante(Estudiantes=Estudiantes):
    cestud = input("Ingrese la cédula del estudiante a editar: ")
    if cestud in Estudiantes:
        while True:
            estud = input("Ingrese los nuevos nombres completos del estudiante: ")
            if estud.count(" ") == 3:
                Estudiantes[cestud]['nombre'] = estud
                print("Información del estudiante editada correctamente.")
                editar_notas = input("¿Desea editar las calificaciones del estudiante? (s/n): ")
                if editar_notas.lower() == 's':
                    calificaciones({cestud: Estudiantes[cestud]})
                    break
                else:
                    print("Calificaciones no editadas.")
            else:
                print("Nombre no valido")
    else:
        print("La cédula ingresada no existe.")
# Check UwU
def tabla(Estudiantes=Estudiantes, Materias=Materias, tamText=tamText):
    estudiantes_ordenados = dict(sorted(Estudiantes.items(), key=lambda item: item[1]['nombre']))

    orden = input("Desea ordenar las materias por la cantidad de estudiantes reprobados?(s/n)")
    if orden.lower() == 's':
        materias_ordenadas = dict(sorted(Materias.items(), key=lambda item: item[1]['numReprobados'], reverse=True))
    else:
        materias_ordenadas = dict(sorted(Materias.items(), key=lambda item: item[1]['materia']))

    tabla = np.empty((len(estudiantes_ordenados) + 1, len(materias_ordenadas) + 1), dtype=object)
    tabla[0, 0] = "" * tamText

    i = 1
    for materia in materias_ordenadas:
        tabla[0, i] = materias_ordenadas[materia]['materia']
        i += 1

    j = 1
    for cedula in estudiantes_ordenados:
        tabla[j, 0] = estudiantes_ordenados[cedula]['nombre']
        k = 1
        for materia in materias_ordenadas:
            tabla[j, k] = estudiantes_ordenados[cedula]['calificaciones'][materias_ordenadas[materia]['materia']]
            k += 1
        j += 1
    print(tabla)
# Revisar!!!!!!!!!!
def graficas():
    global reprobados_ordenados
    print("\nOpciones:")
    print("1. Promedios de Las materias")
    print("2. Numero de estudiantes reprobados por materia")
    print("3. Estudiantes aprobados y reprobados")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    labels = [Materias[m]['materia'] for m in Materias]
    sizes= [Materias[m]['numReprobados'] for m in Materias]
    prom = [Materias[m]['promMat'] for m in Materias]
    
    # Evitar valores NaN en la gráfica de pie
    sizes = [size if size > 0 else 0 for size in sizes]
    
    if opcion == 1:
        plt.bar(labels, prom)
        plt.xlabel("Materias")
        plt.ylabel("Promedio General")
        plt.title("Promedios de Materias")
        plt.show()
    elif opcion == 2:
        colors = plt.cm.Paired(range(len(Materias)))
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
        plt.title("Número de estudiantes reprobados por materia")
        plt.show()
    elif opcion == 3:
        aprobados = sum(1 for est in Estudiantes.values() if est['Estado'] == "Aprobado")
        reprobados = sum(1 for est in Estudiantes.values() if est['Estado'] == "Reprobado")
        estados = ['Aprobados', 'Reprobados']
        cantidad = [aprobados, reprobados]
        fig, ax = plt.subplots()
        ax.pie(cantidad, labels=estados, colors=['blue', 'red'], autopct='%1.1f%%', hatch=['**O', 'O.O'])
        plt.show()
    elif opcion == 4:
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