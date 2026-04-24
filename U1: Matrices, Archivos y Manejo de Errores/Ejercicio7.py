"""
## Ejercicio 7: Mini gestor de usuarios (diccionarios + validaciones)
Importar de un archivo csv una lista con la informacion de usuarios (el archivo tiene las columnas: id, nombre, apellido, email, edad, telefono)
Evitar IDs repetidos, email inválido y edades fuera de rango, telefonos con formato argentino (+54)

Mostrar la informacion del usuario si no tiene errores. En caso de tener errores, escribir eso en un archivo llamado `error_log.txt` donde diga que linea tiene error y el porque del fallo.

Ejemplo: 

```
id,nombre,apellido,email,edad,telefono
0,ana,maria,anamaria@gmail.com,20,+54911123456789 -> Error en el ID
1,juan,perez,juanperez34@gmail,30,+5491112345678 -> Error en el email y el telefono
2,luis,lopez,luislopez@gmail.com,25,+54911123456789 -> Error en el telefono
3,sofia,gome2,sofiagomez17@gmail.com,28,+54911123456789 -> Error en el apellido
4,dieg0,fernandez,diegofernandez@gmail.com,abc,911123456789 -> Error en la edad, el nombre y el telefono
```

Log de errores:
```
Linea 1: Error en el ID
Linea 2: Error en el email y el telefono
Linea 3: Error en el telefono
Linea 4: Error en el apellido
Linea 5: Error en la edad, el nombre y el telefono

```
"""


def validar_email(email):
    usuario, dominio = email.split("@")
    if "." not in dominio:
        return False
    return True

def validar_edad(edad):
    if edad.isdigit() and 0 < int(edad) < 110:
        return True
    return False

def validar_telefono(telefono: str):
    if telefono.startswith("+54911") and len(telefono) == 14:
        return True
    return False

def validar_nombre(nombre):
    return nombre.isalpha()

def validar_apellido(apellido):
    return apellido.isalpha()

def validar_id(id, ids_existentes):
    return id.isdigit() and id in ids_existentes and int(id) > 0

def validar_data(nombre_archivo):
    ids_existentes = []
    pos = 0
    log = open("LOG_ERRORES", "w+")
    with open (nombre_archivo, "r") as file:
        columnas = file.readline()
        for line in file:
            pos+=1
            usuario = line.rstrip("\n").split(",")
            errores = validar_usuario(usuario, ids_existentes)
            ids_existentes.append(usuario[0])
            if errores != []:
                log.write(f"Linea {pos}: Error en {", ".join(errores)}")
    log.close()  

def validar_usuario(usuario: list, ids_existentes): #-> usuario = ["0","ana","maria","anamaria@gmail,com","20","+5491112345678"]
    errores = []
    if not validar_id(usuario[0], ids_existentes):
        errores.append("ID")
    if not validar_nombre(usuario[1]):
        errores.append("Nombre")
    if not validar_apellido(usuario[2]):
        errores.append("Apellido")
    if not validar_email(usuario[3]):
        errores.append("Email")
    if not validar_edad(usuario[4]):
        errores.append("Edad")
    if not validar_telefono(usuario[5]):
        errores.append("Telefono")

    return errores


    
validar_data("./2026/U1: Matrices, Archivos y Manejo de Errores/base_de_datos_usuarios.csv")