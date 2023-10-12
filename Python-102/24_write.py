#Puedo escribir directamente en el archivo, agregando cosas adicionales. Pero, cuando se realiza la función de 'open', el archivo solo me deja leerlo más no editarlos (not writable). Con esto, puedo cambiar la opción y el fin del archivo en el codigo desde la función open agregando 'r' para leer y 'w' para escribir. El problema es que solo se limita a esas funciones y no puedo ejecutarlas al mismo tiempo


'''
with open('./text.txt', 'r') as file:
  for line in file: 
    print(line)
  file.write('nuevas cosas en este archivo')
'''

# En este caso me aparece que no puedo leer lo que hay en el archivo (not readable), con lo cual si regreso al contenido del archivo veo que ya no hay información

'''
with open('./text.txt', 'w') as file:
  for line in file: 
    print(line)
  file.write('nuevas cosas en este archivo')
'''
# Pero ahora como busco realizar ambas funciones, puedo agregar un 'r+' en la funcion open, con lo cual espero leer y editar el archivo al mimso tiempo

'''
with open('./text.txt', 'r+') as file:
  for line in file: 
    print(line)
  file.write('nuevas cosas en este archivo')
'''

# Luego de probar la nueva función leyó el archivo primero y lo imprimio. Pero solo creó una nueva linea despues en el archivo, entonces si me devuelvo al archivo puedo eviudenciar que si hay una nueva linea escrita llamada 'nuevas cosas en este archivo', que esta pegada a la palabra 'Final'. Para ver las lineas con saldto de linea puedo agregarle al final con un \n. Cada que ejecute el codigo se va a poder leer la nueva información
'''
with open('./text.txt', 'r+') as file:
  for line in file: 
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('nueva linea\n')
  file.write('otra mas\n')
'''

# Se puede ver de forma dinámica, cada que lo ejecuto de nuevo se agregan nuevas lineas

# Ahora si quiero reemplazar todo el contenido del texto puedo usar 'w+' en la funcion de open. La operación se ve reflejada en el archivo text.txt, no se ve impreso en la terminal

with open('./text.txt', 'w+') as file:
  for line in file: 
    print(line)
  file.write('más contenido\n')
  file.write('más pruebas\n')
  file.write('Final\n')

# Lo peligroso es que estoy reescribiendo y puedo perder la información anterior