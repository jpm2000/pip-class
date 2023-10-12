file = open('./text.txt')
# Lee todo el texto del archivo
'''
print(file.read())
'''

#Para leerlo linea a linea, no se puede ejecutar al mismo tiempo de la lectura completa del archivo. Es menos pesado, ocupa menos memora y cuando hay mucha información en el archivo puede ser más práctico. 

'''
print(file.readline())
print(file.readline())
print(file.readline())
'''

# El problema es que no se hasta donde termina el readline(), se puede usar un for para hacer un print de cada linea y frena cuando el archivo termina. Con eso le agrego la opción close

for line in file: 
  print(line)

file.close()

#Con esta siguiente opción no tengo que cerrar el archivo, lo hará automáticamente, ya que python lo identifica como un archivo finito

with open('./text.txt') as file:
  for line in file: 
    print(line)


