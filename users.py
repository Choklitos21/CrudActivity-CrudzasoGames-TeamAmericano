import os
import json


if os.path.getsize("users.json") == 0:
        data = []
else:
    with open("users.json", 'r') as old_json:
        data = json.load(old_json)

#REGISTRO DE USUARIO
def crearusuario():

    registro_usuario = True
    registro_clave = True
    
    print("REGISTRO DE USUARIO \n")
    print("El nombre de usuario debe tener entre 4 y 12 caracteres.")
    print("El nombre de usuario debe contener solo letras y/o números, sin espacios. \n")
    while registro_usuario: # bucle while para validacion de registro de usuario

        usuario_ingresado = input("Ingrese su usuario: ").lower()

        if len(usuario_ingresado) < 4 or len(usuario_ingresado) > 12:
            print("Error: El nombre de usuario debe tener entre 4 y 12 caracteres. Inténtelo de nuevo.")
            continue

        if " " in usuario_ingresado:
            print("Error: No se permiten espacios, intentelo de nuevo")
            continue
        
        if not usuario_ingresado.isalnum():
            print("Error: Solo caracteres validos (numeros y letras) \n")
            continue

        existe = False

        for user in data:
            print(user)
            if user["usuario"] == usuario_ingresado:
                existe = True
                break
        
        if existe:
            print("Este usuario ya existe, por favor ingrese uno nuevo \n")
            continue

        registro_usuario = False

        
    print("\nREGISTRO DE CONTRASEÑA \n")
    print("su clave debe ser numérica y tener exactamente 4 dígitos. \n")

    while registro_clave:
        clave_ingresada = input("Ingrese su clave: ")

        if len(clave_ingresada) != 4:
            print("Error: Su clave solo debe tener 4 digitos \n")
            continue


        if not clave_ingresada.isdigit():
            print("Error: Solo se permiten numeros \n")
            continue

        clave_ingresada = int(clave_ingresada)

<<<<<<< HEAD

        registro_clave = False


    nuevo_usuario = {
        "usuario": usuario_ingresado,
        "clave": clave_ingresada,
    }

    
    data.append(nuevo_usuario)

    with open("users.json", "w", encoding="utf-8") as new_json:
        json.dump(data, new_json, indent=4)

    print("\nUsuario registrado correctamente, puede continuar.")


crearusuario()
=======
def crearusuario ():
return user

def iniciarsesion():
return user
>>>>>>> 3d21c26965fda7e5902f1fe2219ee3cfea075d97
