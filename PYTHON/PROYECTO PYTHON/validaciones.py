from gestionarJson import cargar

def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None

def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Nombre vacio")
        return False
    return True
def apellido_valido(apellido):
    if apellido.strip()=="":
        print("Apellido vacio")
        return False
    return True
def telefono_valido(telefono):
    if telefono.strip=="":
         print('Telefono no valido')
         return False
    return True


def ValidarCategoria(categoria):
    if categoria.strip()=="":
        print("Categoría vacio")
        return False
    return True