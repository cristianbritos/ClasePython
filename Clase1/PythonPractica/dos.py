class Persona:

    nombre = ""
    edad = None

    def __init__(self, n, e):
        self.nombre = n
        self.edad = e 


p = Persona("Pablo",30)

print("Mi nombre es: "+ p.nombre)
print("Mi edad es: "+ str(p.edad))
