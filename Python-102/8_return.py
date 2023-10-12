def sum_range(min, max):
  print('min -> ', min, ' max -> ', max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_range(10, 30)
print('first result: ', result)
result_2 = sum_range(result + 50, result + 100)
print('second result: ', result_2)

print('')

suma = 0 
for x in range(1, 10):
  suma += x

print(suma)

print('')

def suma_rango(min, max):
  print(min, max)
  suma = 0
  for x in range(min, max):
    suma += x
  print(suma)

suma_rango(1, 10)


'''
When talking about Return, is when we want to get the result but we just don't want to print it. This allows the computer to use the result in other functions. 
'''

print('')

def rest_range(max, min):
  print(max, min)
  rest = 0
  for x in range(max, min):
    rest -= x
  return rest

result = rest_range(10, 100)

print('rest')
print(result)

print('')

def suma_rango(min, max):
  print(min, max)
  suma = 0
  for x in range(min, max):
    suma += x
    suma_2 = suma * 2
  return suma_2
  
print('suma')
result_1 = suma_rango(1, 10)
print(result_1)


print('')

def mult_range(a, b):
  mult = a * b
  return mult

print('multiplicación')
result_2 = mult_range(500, 2)
print(result_2)

print('')

print('suma total')
print(result_1 + result_2)


print('')


def suma_rango_2(min, max):
  print(min, max)
  suma = 0
  for x in range(min, max):
    suma += x
  return suma
  
print('suma_2')
result_3 = suma_rango_2(10, 100)
print(result_3)

print('')

result_4 = suma_rango_2(result_3 * 3, result_3 * 10)
print('resultado, usando el return dentro de la misma función')
print(result_4)

print('')

def suma_3(min, max):
  suma = 0
  for x in range(min, max):
    suma += x
  return suma

mini = input('put the minimun variable')
maxi = input('write down the maximun variable')

res = suma_3(int(mini), int(maxi))
