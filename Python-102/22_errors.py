
# Va a calcular el error, lo que se busca es hacer un reporte de fallos en otro lado. Atrapar los errores, puedo imprimirlo, capturarlo en un reporte de errores o mostrarlo. Puedo incluir todos los errores en un solo try.

try:
  print(0/0)
except ZeroDivisionError as error:
  print(error)


print('Hola')

try:
  assert 1 != 1, 'Uno es no es igual a uno'
except AssertionError as error:
  print(error)

try:
  age = int(input('how old are you? '))
  if age < 18:
    raise Exception('No se permiten menores de edad')
  if age > 50:
    raise Exception('Ya estas muy viejo')
except Exception as error:
  print(error)


def my_divide(a,b):
  result = a/b
  return result

#Ejercicio

try:
  response = my_divide(10, 2)
  print(response)
  raise ZeroDivisionError('No se puede dividir por 0')

  response = my_divide(10, 0)
  print(response)
  raise ZeroDivisionError('No se puede dividir por 0')
except ZeroDivisionError as error:
  print(error)

print('hola')