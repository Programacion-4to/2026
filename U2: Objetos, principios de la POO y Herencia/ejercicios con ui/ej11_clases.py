# ── Ejercicio 11 — Sistema MercadoLibre ───────────────────────────────────────
#
# Completá cada clase respetando los atributos y métodos indicados.
# Cuando termines, ejecutá ej11_mercadolibre.py para ver tu sistema en acción.
# ─────────────────────────────────────────────────────────────────────────────


class Producto:
    def __init__(self, nombre, precio):
        pass

    def __str__(self):
        # Debe retornar algo como: "Notebook — $1200.00"
        pass


class Usuario:
    def __init__(self, nombre, email, contrasena):
        # _contrasena es un atributo protegido
        pass

    def mostrar_datos(self):
        # Retornar un string con nombre y email
        pass

    def verificar_contrasena(self, contrasena):
        # Retornar True si coincide, False si no
        pass


class Cliente(Usuario):
    def __init__(self, nombre, email, contrasena):
        # Llamar al __init__ del padre con super()
        # Inicializar carrito como lista vacía
        pass

    def agregar_producto_al_carrito(self, producto):
        pass

    def vaciar_carrito(self):
        pass

    def total_carrito(self):
        # Retornar la suma de los precios de todos los productos del carrito
        pass


class Admin(Usuario):
    def __init__(self, nombre, email, contrasena, tienda):
        # Llamar al __init__ del padre con super()
        # Guardar la referencia a la tienda
        pass

    def crear_producto(self, nombre, precio):
        # Crear un Producto, agregarlo a self.tienda y retornarlo
        pass

    def eliminar_producto(self, producto):
        # Eliminar el producto de self.tienda
        pass


class Tienda:
    def __init__(self):
        # Inicializar lista_productos y lista_usuarios como listas vacías
        pass

    def agregar_producto(self, producto):
        pass

    def eliminar_producto(self, producto):
        pass

    def registrar_usuario(self, usuario):
        pass

    def mostrar_productos(self):
        # Retornar la lista de productos
        pass


class App:
    def __init__(self, tienda):
        pass

    def login(self, email, contrasena):
        # Buscar en tienda.lista_usuarios el usuario con ese email
        # Verificar la contraseña con verificar_contrasena()
        # Retornar el usuario si es correcto, None si no
        pass
