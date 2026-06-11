import os,time
from funtions import *
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
        nombre = str(input("Ingrese titulo del libro a buscar: ")).title()
        buscar_libro(nombre)
    elif opcion == 4:
        nombre = str(input("Ingrese titulo del libro a solicitar: ")).title()
        prestar_libro(nombre)
    elif opcion == 5:
        nombre  = str(input("Ingrese titulo del libro a devolver: ")).title()
        devolver_libro(nombre)
    elif opcion == 6:
        nombre = str(input("Ingrese titulo del libro a eliminar: ")).title()
        eliminar_libro(nombre)
        
        print("")
    elif opcion == 7:
        print("")
    elif opcion == 8:
        print("")
    else:
        print("Gracias por su visita")
        break
