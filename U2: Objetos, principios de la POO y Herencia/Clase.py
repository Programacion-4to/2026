import time

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cafeteras = []
    
    def saludar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} anios")

    def comprar_cafetera(self, cafetera):
        self.cafeteras.append(cafetera)

    def hacer_cafe(self, cafe):
        if self.cafeteras == []:
            raise ValueError("No tenes cafeteras master, pedile al momo")
        
        for c in self.cafeteras:
            if not c.get_esta_sucia():
                c.hacer_cafe(cafe)
                return
        
        print("No tengo cafeteras limpias para hacerme el cafe")

    def limpiar_cafetera(self, cafetera):
        cafetera.limpiar_cafetera()

class Cafetera:
    ESTILOS = ["Italiana", "Capsula", "Filtro"]
    def __init__(self, color, estilo, marca):
        self.color = color
        if estilo not in self.ESTILOS:
            raise ValueError("El estilo no existe")
        self.estilo = estilo
        self.marca = marca
        self.esta_sucia = False
    
    def get_esta_sucia(self):
        return self.esta_sucia
    
    def set_color(self, color):
        self.color = color

    def hacer_cafe(self, cafe):
        print(f"Tu cafetera marca {self.marca} esta haciendo un {cafe}...")
        self.esta_sucia = True
        time.sleep(3)
        print(f"Tu {cafe} esta listo!")

    def limpiar_cafetera(self):
        print(f"Limpiando cafetera {self.marca}...")
        time.sleep(2)
        print("Cafetera limpia!")


# facu = Persona("Facundo", "22")
# facu.saludar()
# cafetera1 = Cafetera("Negro", "Italiana", "Bialetti")
# facu.comprar_cafetera(cafetera1)
# facu.hacer_cafe("Cafe con leche")
# facu.limpiar_cafetera(cafetera1)
# facu.hacer_cafe("Cortado")


# EJERCICIO 6 de OBJETOS

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.productos = []
        # self.total_ = 0
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        # self.total_ += producto.precio

    def total(self):
        # return self.total_
        total = 0
        for prod in self.productos:
            total += prod.precio

        return total

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []
        self.pedido_actual = Pedido()

    def hacer_pedido(self):
        if self.pedido_actual.productos == []:
            raise ValueError("Tu pedido esta vacio")
        self.pedidos.append(self.pedido_actual)
        self.pedido_actual = Pedido()
        

    def total_gastado(self):
        total = 0
        for ped in self.pedidos:
            total += ped.total()
        return total

p1 = Producto("Pan", 100)
p2 = Producto("Leche", 200)


cliente = Cliente("Facundo")
cliente.pedido_actual.agregar_producto(p1)
cliente.pedido_actual.agregar_producto(p2)
cliente.hacer_pedido()
cliente.pedido_actual.agregar_producto(p2)
cliente.hacer_pedido()

print(cliente.total_gastado())

