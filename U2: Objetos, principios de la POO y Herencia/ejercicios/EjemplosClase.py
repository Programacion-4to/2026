class Animal:
    def __init__(self, edad, colores):
        self.__edad = edad
        self.colores = colores
        self.tiene_cola = True

    def comer(self):
        ...
    
    def cazar(self):
        ...

    def mover_la_cola(self):
        if self.tiene_cola:
            print("Moviendo la cola")
        else:
            print("No tiene cola")

    def cumplir_anios(self):
        self.__edad +=1

    def hacer_ruido(self):
        pass

class Perro(Animal):
    def __init__(self, edad, colores, raza):
        super().__init__(edad, colores)
        self.raza = raza

    def hacer_ruido(self):
        print("Guau")

    def __str__(self):
        return f"Perro de raza {self.raza}"
    
    def __repr__(self):
        return f"Perro de raza {self.raza}" 


class Dueno:
    def __init__(self, nom, gen, age):
        self.__nombre = nom
        self.__genero = gen
        self.__edad = age
        self.mascotas = []

    def pasear(self):
        if self.mascotas != []:
            print("Paseando...")
        else:
            print(f"Lo siento {self.__nombre}, no tienes mascotas todavia")

    def adoptar(self, animal: Animal):
        if isinstance(animal, Animal):
            self.mascotas.append(animal)


# perrito = Perro(1,"Marron","Caniche")
# perrito.hacer_ruido()
# print(perrito.raza)

# tigre = Animal(4,["Naranja","Negro"])
# tigre.hacer_ruido()


# facundo = Dueno("facundo","M",21)
# facundo.pasear()
# facundo.adoptar(perrito)
# facundo.pasear()
# print(facundo.mascotas)


perro1 = Perro(2,"Blanco","Labrador")
perro2 = Perro(3,"Negro","Pastor Aleman")

print(perro1)

perros = [perro1, perro2]

print(perros)




"""
Dueno -> List[Animal]


"""


