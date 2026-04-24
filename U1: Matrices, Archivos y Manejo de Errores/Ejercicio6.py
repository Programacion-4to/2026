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
    if "@" in email and "." in email:
        return True
    return False

def validar_edad(edad):
    if edad.isdigit() and 0 < int(edad) < 120:
        return True
    return False

def validar_telefono(telefono):
    if telefono.startswith("+54") and len(telefono) == 14:
        return True
    return False

def validar_id(id, ids_existentes):
    if id.isdigit() and id not in ids_existentes:
        return True
    return False

def validar_nombre(nombre):
    if nombre.isalpha():
        return True
    return False

def validar_apellido(apellido):
    if apellido.isalpha():
        return True
    return False

def validar_usuario(usuario, ids_existentes):
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


def registrar_error(mensaje):
    # Si falla la escritura del log, evitamos romper el proceso principal.
    try:
        with open("error_log.txt", "a") as error_file:
            error_file.write(f"{mensaje}\n")
    except OSError:
        print(f"No se pudo escribir en error_log.txt: {mensaje}")

def procesar_usuarios(archivo):
    ids_existentes = set()
    try:
        with open(archivo, "r") as file:
            columnas = file.readline().rstrip("\n").split(",")
            print(f"Esta tabla tiene las columnas: {', '.join(columnas)}")

            for numero_linea, line in enumerate(file, start=2):
                try:
                    usuario = line.rstrip("\n").split(",")

                    if len(usuario) != 6:
                        raise ValueError("Cantidad de columnas invalida")

                    errores = validar_usuario(usuario, ids_existentes)
                    if errores:
                        registrar_error(
                            f"Linea {numero_linea}: Error en {' y '.join(errores)}"
                        )
                    else:
                        ids_existentes.add(usuario[0])
                        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[3]}")
                except (ValueError, IndexError) as error:
                    registrar_error(f"Linea {numero_linea}: Error de formato ({error})")

    except FileNotFoundError:
        print(f"No se encontro el archivo: {archivo}")
    except OSError as error:
        print(f"Error al abrir/leer el archivo: {error}")
