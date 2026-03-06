from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido,apellido_valido,telefono_valido,ValidarCategoria
from gestionlogs import log
from datetime import date
ARCHIVO = "categorias.json"

def guardarCategoria():
    categorias=cargar(ARCHIVO)
    cate=input('Ingrese el nombre de la Hermienta ')
    while nombre_valido(cate)==False or existeNombre(cate)==True:
        cate=input('Ingrese el nombre de la Herramienta valida ')
    herramienta=input('ingrese el numero de herramientas ')
    categoescoger=validarMenu('''
                          dame la categoria de la herramienta
                          1.    construccion 
                          2.    jardineria 
                          3.    mecanica
                       ''',1,3)
    match (categoescoger):
        case 1:
            categoescoger="construccion"
        case 2:
            categoescoger="jardineria"
        case 3:
            categoescoger="mecanica "
        case _:
            print('opcion no encontrada ')
    estado=validarMenu('''
                      Dame el estado de la herramienta 
                       1. buen estado 
                       2. en reparacion 
                       3. fuera de servicio
                    ''',1,3)
    match (estado):
        case 1:
            estado='buen estado '
        case 2:
            estado=' en reparacion '
        case 3:
            estado='fuera de servicio '
        case _:
            print('error opcion no encontrada ')
            
    nueva_categoria={
        "id": generar_id(categorias),
        "nombre": cate,
        "herramienta":herramienta,
        "categoria": categoescoger,
        "estado": estado,
    }
    categorias.append(nueva_categoria)
    guardar(ARCHIVO,categorias)
    print('HERRAMIENTA GUARDADA!')
    log("guardar herramienta", date.today(), "Usuario", id)

       
def listar_categoria():
    catego=cargar(ARCHIVO)
    if not catego:
        print ("No hay categorias\n")
        return
    
    for elemento in catego:
         print(f'ID: {elemento["id"]} -> {elemento["nombre"]} -> {elemento["herramienta"]} -> {elemento["categoria"]} -> {elemento["estado"]}')
    print() 
def existeProfesion(id_categorias):
    lista_categorias=cargar("categorias.json")
    for elemento in lista_categorias:
        if id_categorias==elemento["id"]:
            return True
    return None

def existeNombre(nombre):
    categorias=cargar(ARCHIVO)
    for elemento in categorias:
        if nombre.lower()==elemento["nombre"].lower():
            return True
    return False
    

def actualizar_categoria():
    categorias=cargar(ARCHIVO)
    listar_categoria()
    id_categorias=validarEntero("Escoja el id a actualizar ")
    while(id_categorias==None):
        id_categorias=validarEntero("Error, Escoja el id a actualizar ")
        
    for elemento in categorias:
        if id_categorias==elemento["id"]:
            nombre=input('Ingrese el nombre de la herramienta ')
            while nombre_valido(nombre)==False:
                nombre=input('Ingrese el nombre de la herramienta ')
            herramienta=input('ingrese el numero de herramientas ')
            categoescoger=validarMenu('''
                          Dame la categoria de la herramienta
                          1.    construccion 
                          2.    jardineria 
                          3.    mecanica
                       ''',1,3)
            match (categoescoger):
             case 1:
              categoescoger="construccion"
             case 2:
               categoescoger="jardineria"
             case 3:
               categoescoger="mecanica "
             case _:
              print('opcion no encontrada ')
        estado=validarMenu('''
                      Dame el estado de la herramienta 
                       1. buen estado 
                       2. en reparacion 
                       3. fuera de servicio
                    ''',1,3)
        match (estado):
         case 1:
            estado='buen estado '
         case 2:
            estado=' en reparacion '
         case 3:
            estado='fuera de servicio '
         case _:
            print('error opcion no encontrada ')
            elemento["nombre"]=nombre
            elemento["herramienta"]=herramienta
            elemento["categoria"]=categoescoger
            elemento["estado"]=estado
            guardar(ARCHIVO,id_categorias)
            print('Categoria actualizada!')
            log("actualizar herramienta", date.today(), "Usuario", id)
            return
        print("La categoria no existeb ")
        log("no se actualizo categoria", date.today(), "Usuario", id)

def eliminar_categoria():
    contador_aux=0
    categorias=cargar(ARCHIVO)
    listar_categoria()
    id_categorias=validarEntero("Escoja el id a eliminar")
    while(id_categorias==None):
        id_categorias=validarEntero("Error, Escoja el id a eliminar")
        
    for elemento in categorias:
        if id_categorias==elemento["id"]:
            categorias.pop(contador_aux)
            guardar(ARCHIVO, categorias)
            print('Categoria eliminada!')
            log("eliminar categoria", date.today(), "Usuario", id)
            return
        contador_aux+=1
    print("Las categorias no existe")
    log("no se elimino categoria ", date.today(), "Usuario", id)

    
    