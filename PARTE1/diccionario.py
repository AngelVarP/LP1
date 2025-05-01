from tabulate import tabulate

# Definimos un diccionario vacio 
AlumnoD = {}

# FUNCIONES A UTILIZAR

# Funcion para definir codigo (Modulo11)
def modulo11():
    while True:
        cod = int(input("Codigo del alumno (6 digitos): "))

        # Validar 6 cifras
        if len(cod) == 6 and cod.isdigit():
            cod = int(cod)
            break
        else: 
            print("El codigo debe tener exactamente 6 digitos. Por favor, intanta nuevamente.")

    t = 1
    aux = cod
    suma = 0

    while t <= 6:
        digito = cod % 10
        peso = 8 - t
        suma = suma + peso * digito
        cod = cod // 10
        t = t + 1

    mod11 = suma % 11
    equivalencias = ""

    if mod11 == 0:
        equivalencias = "0"
    elif mod11 == 1:
        equivalencias = "A"
    elif mod11 == 2:
        equivalencias = "B"
    elif mod11 == 3:
        equivalencias = "C"
    elif mod11 == 4:
        equivalencias = "D"
    elif mod11 == 5:
        equivalencias = "E"
    elif mod11 == 6:
        equivalencias = "F"
    elif mod11 == 7:
        equivalencias = "G"
    elif mod11 == 8:
        equivalencias = "H"
    elif mod11 == 9:
        equivalencias = "I"
    elif mod11 == 10:
        equivalencias = "J"

    nuevoCodigo = str(aux) + equivalencias 
    return nuevoCodigo

# Funcion para agregar alumnos al diccionario
def agregarAlumno():
    codigo = modulo11()
    apellido = input("Ingresa el apellido del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    edad = int(input("Ingresa la edad del alumno: "))

    AlumnoD[codigo] = {"Apellido": apellido, "Nombre": nombre,"Edad": edad}
    print("Alumno agregado con codigo: ",codigo)

# Funcion para mostrar reporte
def mostrarReporte():
    if len(AlumnoD) == 0:
        print("No hay alumnos matriculados.")
        return
    
    # Preparamos los datos de los alumnos
    alumnosLista = []
    for index, (codigo, datos) in enumerate(AlumnoD.items(), start=1):
        alumnosLista.append([index, codigo, datos['Apellido'], datos['Nombre'], datos['Edad']])

    # Encabezados de la tabla
    encabezados = ["#","Código", "Apellido", "Nombre", "Edad"]
    
    # Mostrar la tabla con tabulate
    print("\nReporte de Alumnos:")
    print(tabulate(alumnosLista, headers=encabezados, tablefmt="grid"))

# Funcion para mostrar menu de opciones
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar alumno")
        print("2. Mostrar reporte de alumnos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregarAlumno()
        elif opcion == "2":
            mostrarReporte()
        elif opcion == "3":
            print("Programa Finalizado...")
            break
        else:
            print("Opcion no valida, intenta nuevamente")


# Ejecucion del programa
menu()