from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido,telefono_valido
from gestionarherramienta import listar_categoria
from datetime import date
from gestionlogs import log

ARCHIVO = "persona.json"

def guardar_persona():
    personas=cargar(ARCHIVO)

    nombre=input('Ingrese el nombre de la persona ')
    while nombre_valido(nombre)==False:
        nombre=input('Ingrese el nombre de la persona valida ')
    apellido=input('ingresa el apellido ')
    while nombre_valido(apellido)==False:
        apellido=input('ingresa nuevamente el apellido de la persona valida ')
    telefono=input('ingresa el telefono de la persona ')
    while telefono_valido(telefono)==False:
        telefono=input('ingresa nuevamente el telefono de la persona valida ')
    direccion=input('ingrese la direccion de la persona ')
    nueva_persona={
        "id": generar_id(personas) ,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
    }
    personas.append(nueva_persona)
    guardar(ARCHIVO,personas)
    print('PERSONA GUARDADA!')
    log("guardar persona", date.today(), "Usuario", id)

def listar_persona():
    categorias=cargar(ARCHIVO)
    if not categorias:
        print ("No hay personas\n")
        return
    
    for elemento in categorias:
        print(f'ID: {elemento["id"]} -> {elemento["nombre"]} -> {elemento["apellido"]} -> {elemento["telefono"]} -> {elemento["direccion"]}')
    print()
def actualizar_persona():
    categorias=cargar(ARCHIVO)
    listar_persona()
    id_categorias=validarEntero("Escoja el id a actualizar ")
    while(id_categorias==None):
        id_categorias=validarEntero("Error, Escoja el id a actualizar ")
    for elemento in categorias:
        if id_categorias==elemento["id"]:
            nombre=input('Ingrese el nombre de la Persona ')
            while nombre_valido(nombre)==False:
                nombre=input('Ingrese el nombre de la Persona ')
            apellido=input('ingresa el apellido ')
            while nombre_valido(apellido)==False:
             apellido=input('ingresa nuevamente el apellido de la persona valida ')
            telefono=input('ingresa el telefono de la persona ')
            while telefono_valido(telefono)==False:
             telefono=input('ingresa nuevamente el telefono de la persona valida ')
            direccion=input('ingrese la direccion de la persona ')
            elemento["nombre"]=nombre
            elemento["apellido"]=apellido
            elemento["telefono"]=telefono
            elemento["direccion"]=direccion
            guardar(ARCHIVO, id_categorias)
            print('Categoria actualizada!')
            log("listar persona", date.today(), "Usuario", id)
            return
    print("La categoria no existe. \n")
def existecategoria(id_categorias):
    lista_categorias=cargar("categorias.json")
    for elemento in lista_categorias:
        if id_categorias==elemento["id"]:
            return True
    return None

def eliminar_persona():
    contador_aux=0
    personas=cargar(ARCHIVO)
    listar_persona()
    id_persona=validarEntero("Escoja el id a eliminar")
    while(id_persona==None):
        id_persona=validarEntero("Error, Escoja el id a eliminar")
        
    for elemento in personas:
        if id_persona==elemento["id"]:
            personas.pop(contador_aux)
            guardar(ARCHIVO, personas)
            print('Persona eliminada!')
            log("eliminar persona", date.today(), "Usuario", id)
            return
        contador_aux+=1
    print("La persona no existe")
    log("persona no fue eliminada", date.today(), "Usuario", id)
    
    