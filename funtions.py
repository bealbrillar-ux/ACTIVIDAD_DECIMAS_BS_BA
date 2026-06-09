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