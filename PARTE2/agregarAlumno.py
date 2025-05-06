import os
from comandoVoz import voz

# Función para generar el código del alumno 
def modulo11(codigo):
    t = 1
    aux = int(codigo)
    suma = 0
    while t <= 6:
        digito = aux % 10
        peso = 8 - t
        suma += peso * digito
        aux = aux // 10
        t += 1

    mod11 = suma % 11
    equivalencias = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return codigo + equivalencias[mod11]

# Función para ingresar una nota válida
def validarNota(nota):
    while True:
        try:
            valorNota = float(input(f"Ingrese la {nota} (0-20): "))
            if 0 <= valorNota <= 20:
                return valorNota
            else:
                print("La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entre 0 y 20.")

# Funcion para validar existencia del alumno
def verificarExistencia(codigo):
    if os.path.exists("lista.txt"):
        with open("lista.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(codigo):  # Verifica si el código ya existe
                    return True  
    return False  

# Función para agregar un alumno
def agregarAlumno():
    # Verificar si el archivo lista.txt existe
    if not os.path.exists("lista.txt"):
        # Si el archivo no existe, lo creamos 
        with open("lista.txt", "w") as file:
            file.write("Codigo | Apellido | Nombre | PC1 | PC2 | PC3 | PC4 | Promedio | Estado\n")

    while True:
        # Solicitar datos del alumno
        codigo = input("Ingrese el codigo del alumno (6 dígitos): ")

        # Validar que el código tenga 6 dígitos
        if len(codigo) != 6 or not codigo.isdigit():
            print("El código debe ser de 6 dígitos.")
            continue
        
        if verificarExistencia(codigo):
            print("El alumno ya existe.")
            continue

        # Generar el código con Módulo 11
        newCodigo = modulo11(codigo)
        
        apellido = input("Apellido del alumno: ")
        nombre = input("Nombre del alumno: ")
        
        # Ingresar notas
        pc1 = validarNota("Nota PC1")
        pc2 = validarNota("Nota PC2")
        pc3 = validarNota("Nota PC3")
        pc4 = validarNota("Nota PC4")
        
        # Eliminar la menor nota y calcular el promedio
        notas = [pc1, pc2, pc3, pc4]
        notas.remove(min(notas))  
        promedio = sum(notas) / 3  

        # Determinar el estado
        if promedio >= 10:
            estado = "Aprobado"
        else:
            estado = "Desaprobado"

        # Escribir los datos del alumno en el archivo lista.txt
        with open("lista.txt", "a") as file:
            file.write(f"{newCodigo} | {apellido} | {nombre} | {pc1} | {pc2} | {pc3} | {pc4} | {promedio} | {estado}\n")
        
        print(f"Alumno {nombre} {apellido} agregado con éxito. Codigo: {newCodigo}")
        voz(f"Alumno {nombre} {apellido} agregado con éxito. Codigo: {newCodigo}")
    
