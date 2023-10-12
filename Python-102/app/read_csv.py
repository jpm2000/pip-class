

# Es importante que cuando voy a abrir el archivo, en la funcion delimiter, debo ir al archivo para ver si los datos están separados por ',' o ';'
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      print('')
      print(row)

if __name__ == '__main__':
  read_csv('./app/data.csv')
'''


# La información llega como una lista, lo cual dificulta la lectura de la información. Con esto lo que busco realizar es cambiar la forma en la que el csv se interpreta, pasando de listas a formatos de diccionarios, en donde el nombre es la llave
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    print(header)

if __name__ == '__main__':
  read_csv('./app/data.csv')
'''

# Anteriormente lo que hice fue sacar todos los headers para luego conectarlos con los row. Con esto se deben unir dos arraise con los iterables. Usar el header con el row que corresponda. Esto se hace con un zip, union del header con el row. Y ahora tengo ub array como tuplas
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    for row in reader:
      iterable = zip(header, row)
      print(list(iterable))

if __name__ == '__main__':
  read_csv('./app/data.csv')
'''

import csv

# Ahora para crear el diccionario, debo hacerlo con dictionary comprehension 
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
'''
# Los csv nos entrega la información en listas, más es importante manipular e interpretar la información como un diccionario. La llave es el nombre de la columna

def read_csv(path):
  with open(path, 'r') as csvfile:
    # El reader es un iterable
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])


'''
['33', 'ARG', 'Argentina', 'Buenos Aires', 'South America', '45510318', '45036032', '43257065', '41100123', '37070774', '32637657', '28024803', '23842803', '2780400', '16.3683', '1.0052', '0.57']
'''
