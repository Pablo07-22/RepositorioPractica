from validaciones import validarMenu
from gestionarherramienta import guardarCategoria,actualizar_categoria,eliminar_categoria,listar_categoria
from gestionarPersona import guardar_persona, eliminar_persona, listar_persona,actualizar_persona
from gestionarprestamo import solicitud_prestamo, listar_solicitudes
def categori():
    while True:
        op2=validarMenu('''
                            1. Agregar Persona
                            2. Actualizar Persona
                            3. Eliminar Persona
                            4. Listar Persona
                            5. Salir
                            ''',1,5)
        while op2==None:
                op2=validarMenu('Error, intente nuevamente!',1,5)

        match op2:
            case 1:
                guardar_persona()
            case 2:
                actualizar_persona()
            case 3:
                eliminar_persona()
            case 4:
                listar_persona()
            case 5:
                print('Gracias por ingresar, chao')
            case _:
                print('No se encontró la opción.')
        if op2==5:
            break

def person():
    while True:
        op5=validarMenu('''
                            1. Agregar Herramienta
                            2. Actualizar Herramienta
                            3. Eliminar Herramienta
                            4. Listar Herramienta
                            5. Salir
                            ''',1,5)
        while op5==None:
                op5=validarMenu('Error, intente nuevamente!',1,5)
        match op5:
            case 1:
                guardarCategoria()
            case 2:
                 actualizar_categoria()
            case 3:
                eliminar_categoria()
            case 4:
                listar_categoria()
            case 5:
                print('Chao gracias')
            case _:
                print('No se encontró la opción.')
        if op5==5:
            break




def menu():
 while True:
     op3=validarMenu('''Ingresa tu cargo
                         1. Administrador 
                         2. Usuario
                         3. salir 
                         ''',1,3)
     match op3:
            case 1:
                contraseña=1234
                correccion=int(input('Ingresa la contraseña del administrador'))
                if correccion!=contraseña:
                    correccion=int(input('Clave incorrecta, reintente'))  
                else: 
                    print('Clave correcta, Bienvenio')  
                op0=validarMenu('''
                     QUE QUIERES HACER ?
                        1. Agregar Persona 
                        2. Agregar Herramienta
                        3. ver solicitudes         
                        4. Salir
                    ''',1,3)   
                match op0:
                       case 1:
                         categori()
                       case 2:
                         person()
                       case 3:
                          listar_solicitudes()
                       case 4:
                          print('Gracias por ingresar')
                          menu()
                       case _:
                         print('NO SE ENCUENTRA LA OPCION')
                if op0==4: 
                    break
            case 2:
                op9=validarMenu('''
                                Seleciona una opcion
                                  1. Pedir Herramienta 
                                  2. lista de herramientas 
                                  3 . salir 
                                   ''',1,5)
                match op9:
                     case 1:
                          solicitud_prestamo()
                     case 2:
                          listar_categoria()
                     case 3:
                          print('Gracias por ver chao ')
                          menu()
                     case _: 
                          print('Opcion no encontrada ')
                if op9==3:
                    break
                    
            case 3:
                  print('Gracias por ingresar ')
            case _:
               print('Opcion no valida') 
     if op3==3:
      break         
     