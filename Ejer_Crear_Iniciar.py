import json

def leer_diccionario():
    fichero = open("usuarios.txt")
    usuarios = json.load(fichero)
    fichero.close()
    return usuarios

def guardar_diccionario(usuarios):
    fichero = open("usuarios.txt","w")
    json.dump(usuarios, fichero)
    fichero.close()

def iniciar_sesion():
        while True:
            id = input("Nombre de Usuario: ")
            password = input("Contraseña: ")

            if id in usuarios and password == usuarios[id]:
                print("Bienvenido")
                break
            else:
                print("Usuario o Coontraseña no existente\nIntentelo de nuevo\n")

def crear_cuenta():
    id = input("Nombre de Usuario: ")
    password = input("Contraseña: ")
    usuarios[id] = password
    print("Usuario", id, "fue creado")

usuarios = leer_diccionario()

while True:
    print("""Seleccion una Opción: 
    1: Crear Cuenta 
    2: Iniciar Sesión 
    """)
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        crear_cuenta()
        print("Ahora incia Sesión \n")
        guardar_diccionario(usuarios)
        iniciar_sesion()
        break
    
    elif opcion == "2":
        iniciar_sesion()
        break

    else: 
        print("Opción Incorrecta")
