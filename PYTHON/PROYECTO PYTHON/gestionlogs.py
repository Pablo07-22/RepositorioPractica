from gestionarJson import cargar, guardar, generar_id


LOGS="gestionarlogs.json"

def log(accion, fecha, usuario, id):
    lista=cargar(LOGS)
    lista.append({
        "accion":accion,
        "fecha": str(fecha),
        "usuario": usuario,
        "id":generar_id(lista)
        })
    guardar(LOGS, lista)

def listarlogs():
    logs=cargar(LOGS)
    for elementos in logs:
        print(f"accion:{elementos.get("accion", "el atributo no existe(Accion)")}")
        print(f"fecha:{elementos.get("fecha", "el atributo no existe(fecha)")}")
        print(f"usuario:{elementos.get("usuario", "el atributo no existe(usuario)")}")
        print(f"id:{elementos.get("id ", "el atributo no existe(id)")}")
        