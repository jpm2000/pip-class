# primer ejemplo de error: print(0/0)

# print(result)
print('Hola')
# Siempre que python encuentra un error, para el codigo

suma = lambda x, y : x + y
# Me ayuda a verificar
assert suma(2,2) == 4
# assert suma(2,2) == 5

print('Hola 2')

# puedo lanzar un error, personalizado. Luego de que salga el error el codigo se detiene
age = 10 
if age < 18:
  raise Exception('No se permiten menores de edad')