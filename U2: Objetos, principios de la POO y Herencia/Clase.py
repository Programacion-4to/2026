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


facu = Persona("Facundo", "22")
facu.saludar()
cafetera1 = Cafetera("Negro", "Italiana", "Bialetti")
facu.comprar_cafetera(cafetera1)
facu.hacer_cafe("Cafe con leche")
facu.limpiar_cafetera(cafetera1)
facu.hacer_cafe("Cortado")