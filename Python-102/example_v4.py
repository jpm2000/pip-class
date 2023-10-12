'''
Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.
'''

def filter_by_length(words):
   # Escribe tu solución 👇
   return []

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

num = list(filter(lambda x : len(x) >= 4, words))
print(num)