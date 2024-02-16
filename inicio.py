class animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def pasear(self):
        pass

    def alimentar(self):
        pass

    def dar_info(self):
        return self.nombre + " de raza " + self.raza
class mascota():
    def __init__(self, nombre, raza, propietario):
        super.__init__(, nombre, raza)
        self.nombre=nombre
        self.raza=raza
        self.propietario=propietario 
class gato(animal, mascota):
    def pasear(self):
        print("Paseando al gato " + self.dar_info() + " " + self.propietario)

    def alimentar(self):
        print("alimentando al gato " + self.dar_info() + " " + self.propietario)

class perro(animal, mascota):
    def pasear(self):
        print("Paseando al perro " + self.dar_info() + " " + self.propietario)

    def alimentar(self):
        print("alimentando al perro " + self.dar_info() + " " + self.propietario)

class lagarto(animal, mascota):
    def pasear(self):
        print("Paseando al lagarto " + self.dar_info() + " " + self.propietario)

    def alimentar(self):
        print("alimentando al lagarto " + self.dar_info() + " " + self.propietario)

if __name__ == '__main__':
    mascotas = [perro("Sasha", "Labrador", "Santiago"), gato("Yuumi", "Calico", "Juan"), lagarto("Coco", "cocodrilo", "Pedro")]
    for m in mascotas:
        m.pasear()
        m.alimentar()
