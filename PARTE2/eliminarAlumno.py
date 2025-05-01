from comandoVoz import voz

# Función para eliminar un alumno por su código
def eliminarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a eliminar: ")

    # Leer los datos del archivo lista.txt
    with open("lista.txt", "r") as file:
        lines = file.readlines()

    # Eliminar el alumno con el código ingresado
    encontrado = False
    with open("lista.txt", "w") as file:
        for line in lines:
            if not line.startswith(codigoBuscar):
                file.write(line)  
            else:
                encontrado = True
    
    if encontrado:
        print(f"Alumno con código {codigoBuscar} eliminado exitosamente.")
        voz(f"Alumno con código {codigoBuscar} eliminado exitosamente.")
    else:
        print("Alumno no encontrado.")