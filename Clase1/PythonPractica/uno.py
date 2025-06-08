class Persona:
    nombre  = None
    edad = None

    def __init__(self, nom, e):
        self.nombre = nom
        self.edad = e
            

    def Saludar(self):
        print("Hola, soy "+self.nombre)

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


p = Persona("Cristian",50)

print(f"Nombre: {p.nombre}")
print("Edad: "+str(p.edad))

print("--------")

p.Saludar()

print("--------")

print(p)
