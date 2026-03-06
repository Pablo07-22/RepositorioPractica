from gestionarJson import guardar, cargar, generar_id
from datetime import datetime, timedelta
from gestionarPersona import listar_persona
from gestionarherramienta import listar_categoria,guardarCategoria
from validaciones import validarEntero, validarMenu
from gestionarherramienta import guardarCategoria
from datetime import date
from gestionlogs import log

HERRAMIENTA="herramientas.json"

def solicitud_prestamo():

    herramientas = cargar(HERRAMIENTA)

    print(" USUARIOS ")
    listar_persona()
    listar_categoria()
    listar_prestamos()

    id_usuario = validarEntero('Ingrese el ID del usuario: ')
    while id_usuario is None:
        id_usuario = validarEntero('Error, intentelo nuevamente: ')

    print(' HERRAMIENTAS')
    listar_categoria()

    id_herramienta = validarEntero('Ingrese el ID de la herramienta: ')
    
    while id_herramienta is None:
        id_herramienta = validarEntero('Error, intentelo nuevamente: ')

    cantidad_solicitada = validarEntero("Ingrese la cantidad que necesita: ")
    while cantidad_solicitada is None or cantidad_solicitada <= 0:
        cantidad_solicitada = validarEntero("Error, ingrese una cantidad valida: ")

    dias = validarEntero('Ingrese la cantidad de dias que necesita la herramienta: ')
    while dias is None or dias <= 0:
        dias = validarEntero('Error, intentelo nuevamente: ')
    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=dias)

    nuevo_prestamo = {
        "id": generar_id(herramientas),
        "id_usuario": id_usuario,
        "id_herramienta": id_herramienta,
        "cantidad": cantidad_solicitada,
        "fecha_inicio": str(fecha_inicio.isoformat()),
        "fecha_fin": str(fecha_fin.isoformat()),
        "estado": "pendiente"
    }

    herramientas.append(nuevo_prestamo)
    guardar(HERRAMIENTA, herramientas)

    print("Solicitud de prestamo creada con exito!")
    log("guardar herramienta", date.today(), "Usuario", id)

def listar_prestamos():
    categorias=cargar(HERRAMIENTA)
    if not categorias:

        print("No hay prestamos ")
        log("listar prestamos ", date.today(), "Usuario", id)
        return 
    for elemento in categorias:
        for elemento in categorias:
            print(f'ID: {elemento["id"]} ->  ID Herramienta: {elemento["id_herramienta"]} ->   Cantidad: {elemento["cantidad"]} -> {elemento["fecha_fin"]}')
    print()

def listar_solicitudes():
    contador_aux=0
    personas=cargar(HERRAMIENTA)
    herramientas = cargar(HERRAMIENTA)
    listar_prestamos()
    listar_categoria()
    id_persona=validarEntero("Escoja la lista a aceptar ")
    while(id_persona==None):
        id_persona=validarEntero("Error, Escoja el id a eliminar")
        
    for elemento in personas:
        if id_persona==elemento["id"]:
            personas.pop(contador_aux)
            guardar(HERRAMIENTA, personas)
            print('Solicitud aceptada')
            return
        contador_aux+=1
    print("La herramienta no existe ")
    
   
   

    