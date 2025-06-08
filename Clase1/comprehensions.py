# Comprehensions
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# List Comprehensions

lista_numeros = list(range(100))

print(lista_numeros

pares = [numero for numero in lista_numeros if numero % 2 == 0]

print(pares)

# Dict Comprehensions

studens_uid = [1,2,3]

studens = ['Fatima', 'Maria', 'Nany']

studens_with_uid = {uid : studen for uid, studen in zip(studens_uid, studen)}

print(studens_with_uid)
