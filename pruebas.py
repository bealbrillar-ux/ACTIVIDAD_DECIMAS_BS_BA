


libros = []


for i in range(2):
    acceso = True
    while acceso:
        duplicado = False
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
    libro = {
        "titulo":titulo,
        "autor":autor,
    }
    libros.append(libro)