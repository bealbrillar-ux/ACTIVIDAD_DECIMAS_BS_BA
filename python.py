import os,time
from funciones import *
os.system("cls")

acceso = True
libros = []

while acceso:
    
    print("===== BIBLIOTECA =====")
    print("")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Modificar libro")
    print("8. Mostrar estadísticas")
    print("9. Salir")
    
    opcion = 0
    while opcion not in [1,2,3,4,5,6,7,8,9]:
        try:
            opcion = int(input("Ingrese opcion del menu: "))
        except:
            print("Datos no validos, intente nuevamente")
            time.sleep(1)
    if opcion == 1:
        libros.append(agregar_libro())
        print(libros)
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        nombre = str(input("Ingrese nombre de libro a buscar: "))
        buscar_libro(nombre)
    elif opcion == 4:
        print("")
    elif opcion == 5:
        print("")
    elif opcion == 6:
        print("")
    elif opcion == 7:
        print("")
    elif opcion == 8:
        print("")
    else:
        print("Gracias por su visita")
        break
