# Aca lo que se está haciendo es agregando numeros o valores a una lista, primero se crea la lista, que en este caso no tiene nada y luego con .append se agregan las variables 

print('Initial list V1')
numbers = []
for element in range(1, 11):
  numbers.append(element)

print(numbers)

'''
In this case what I'm doing is taking an element from a for that's in a range
For example
[element * 2 for element in range(1, 11)]
Element      Ciclo donde se extraen 
            elementos de cualquier iterable
'''
print('')
print('Initial list V2')
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

print('')
print('V1')
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

'''
If I want to create the list with a new contition in the element for, I can add an if

Example:
[i* 2 for i in range(1, 11) if i % 2 ==0]
Element      Ciclo donde        Condición opcional
             se extraen         opcional para 
             elementos de       filtrar elementos
             cualquier 
             iterable
'''
print('')
print('V2')

numbers = []
for element in range(1, 11):
  if element % 2 == 0:
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_v2)