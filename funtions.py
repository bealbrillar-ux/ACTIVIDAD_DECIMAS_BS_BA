import time
libros = []

#OPCION 1
def agregar_libro():
    acceso = True
    duplicado = False
    while acceso:
        titulo = str(input("Ingrese el titulo del libro: ")).title()
        for x in libros:
            if x["titulo"] == titulo:
                duplicado = True
        if duplicado:
                print("El libro esta duplicado.")
        else:
            duplicado = False  
            acceso = False        
    autor = str(input("Ingrese el auto del libro: ")).title()
    estado = True
    libro = {
        "titulo":titulo,
        "autor":autor,
        "estado":estado,
    }
    libros.append(libro)
    return libro

#opcion 2
def mostrar_libros():
    if len(libros) > 0:
        for x in libros:
            print(f"\nTitulo: {x["titulo"]}")
            print(f"Autor: {x["autor"]}")
            print(f"Estado: {x["estado"]}")
            print("**************")
            time.sleep(2)
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)

#opcion 3
def buscar_libro(nombre):
    encontrado = False
    if len(libros) > 0:
        for x in libros:
            if x["titulo"] == nombre:
                encontrado = True
            if encontrado:
                print(f"\nTitulo: {x["titulo"]}")
                print(f"Autor: {x["autor"]}")
                print(f"Estado: {x["estado"]}\n")
            else:
                print("Libro a buscar no ha sido encontrado en la biblioteca.")
                time.sleep(1)
                
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)

#opcion 4
def prestar_libro(nombre):
    encontrado = False
    if len(libros) > 0:
        for x in libros:
            if x["titulo"] == nombre:
                encontrado = True
            if encontrado:
                if x["estado"]:
                    x["estado"] = False
                    print("El libro a sido prestado con exito.")
                    time.sleep(1)
                else:
                    print("El libro no esta disponible.")
                    time.sleep(1)
            else:
                print("Libro a buscar no ha sido encontrado en la biblioteca.")
                time.sleep(1)
                
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)

#opcion 5
def devolver_libro(nombre):
    encontrado = False
    if len(libros) > 0:
        for x in libros:
            if x["titulo"] == nombre:
                encontrado = True
            if encontrado:
                if not x["estado"] :
                    x["estado"] = True
                    print("El libro a sido prestado con exito.")
                    time.sleep(1)
                else:
                    print("El libro no esta disponible.")
                    time.sleep(1)
            else:
                print("Libro a buscar no ha sido encontrado en la biblioteca.")
                time.sleep(1)
                
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)
        
#opcion 6
def eliminar_libro(nombre):
    if len(libros) > 0:
        flag1 = False
        for x in libros:
            if x["libro"] == nombre:
                libros.remove(x)
                flag1 = True
            if flag1:
                print("Libro eliminado con exito.")
                time.sleep(1)
            else:
                print("Libro no encontrado en la biliboteca.")
                time.sleep(1)
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)
#opcion 7
def modificar_libro(nombre):
    if len(libros) > 0:
        flag2 = False
        for x in libros:
            if x["libro"] == nombre:
                nuevo_nombre = str(input("Ingrese nuevo titulo del libro: ")).title()
                nuevo_autor = str(input("Ingrese nuevo autor: ")).title()
                if x["titulo"] == nuevo_nombre:
                    print("El libro a modificar tiene el mismo nombre ")
                elif x["autor"] == nuevo_autor:
                    print("El libro a modificar tiene el mismo autor")
                else:
                    x["titulo"] = nuevo_nombre
                    x["autor"] = nuevo_autor
                flag2 = True
            if flag2:
                print("Libro ha sido modificado con exito.")
                time.sleep(1)
            else:
                print("Libro no encontrado en la biliboteca.")
                time.sleep(1)
    else:
        print("No se han agregado libros aun.")
        time.sleep(1)
        
#opción 8
def mostrar_estadisticas(nombre):
    total = len(libros)
    contador_disponibles = 0
    contador_prestados = 0
    for x in libros:
        if x["estado"] == True:
            contador_disponibles += 1
        else:
            contador_prestados += 1
    print(f"Cantidad total de libros: {total}")
    print(f"Cantidad de libros disponibles: {contador_disponibles}")
    print(f"Cantidad de libros prestados: {contador_prestados}")