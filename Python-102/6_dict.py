'''
If I want to create the dictionary with a new contition in the element for, I can add an if

Example:
{i* 2 for i in range(1, 11) if i % 2 ==0}
Element      Ciclo donde        Condición opcional
             se extraen         opcional para 
             elementos de       filtrar elementos
             cualquier 
             iterable
'''

import random

# Otra vez se maneja el ejemplo de crear el diccionario de la poblacion en ciertos países

countries_V2 = ['col', 'mex', 'us', 'per', 'bol', 'arg', 'bra']
population_V2 = {country : random.randint(1, 100) for country in countries_V2}
print(population_V2)

# Aca lo que se realizó fue usar el diccionario creado con anterioridad y buscar cuales tienen una poblacion mayor a 50

result = {country : population for (country, population) in population_V2.items() if population > 50}
print(result)

print('')
print('vocals')
text = 'My name is JPM and I love cycling'
vocals = {c : c.upper() for c in text if c in 'aeiou'}
print(vocals)

#Exercise
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [num for num in numbers if num % 2 == 0]

print('v2 =>', even_numbers_v2)


'''
Summary List VS Tuple VS Set
List, mutable, with an order, indexing/slicing, duplicated elements
Tuple not mutable, with an order, indexing/slicing, duplicated elements
Set mutable, not with an order, no indexing/slicing, no  duplicated elements
'''

order = [1,2,3,4,5,6,7,8,9]
names = ['Simon', 'JP', 'Alejandro', 'Jimena', 'Desconocido', 'Nicolas', 'Siete', 'Luz', 'Juan']
ages = [22,13,22,44,31,32,11,55,66]
people = {ord : name for ord, name in zip(order, names)}
print(people)

period = ['between 1 and 20', 'between 21 and 30', 'between 31 and 40', 'between 41 and 50', 'beyond 51']
result = {}
for age, per in zip(ages, period):
  if age >= 1 and age <= 20:
    per = int(period[0])
    result[age] = per
  elif age >=21 and age <= 30:
    per = int(period[1])
    result[age] = per
  elif age >=31 and age <= 40:
    per = int(period[2])
    result[age] = per
  elif age >=41 and age <= 50:
    per = int(period[3])
    result[age] = per
  else:
    per = int(period[4])
    result[age] = per

print(result)

final = people | result
print(final)

# Terminar luego