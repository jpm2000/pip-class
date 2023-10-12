# Ahora le estoy agregando valores a un diccionario. El valor de i es representado como el key o label y cuando lo igualo a i*2 estoy determinando cual va a ser la variable que va a llevar esa key

print('V1')
numbers = {}
for i in range(1, 5):
  numbers[i] = i*2
print(numbers)

print('')
print('V2')
numbers_V2 ={i:i*2 for i in range(1,5)} 
print(numbers_V2)

print('')
import random 

# En este caso lo que busco realizar es juntar unas keys que ya estan definidas por medio de una lista (que tengo que pasar a un diccionario) y agregar sus respectivas poblaciones. Para no hacer tantos calculos se usa una funcion de random

print('V3 countries 1')
countries = ['col', 'mex', 'us', 'per', 'bol']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

print('')
print('V3 countries 2')
countries_V2 = ['col', 'mex', 'us', 'per', 'bol', 'arg', 'bra']
population_V2 = {country : random.randint(1, 100) for country in countries_V2}
print(population_V2)

print('')
print('V4 name and age 1')
name = ['JP', 'Santi', 'Simon', 'Juan']
age = [22, 30, 40, 10]
print(list(zip(name, age)))

print('')
print('V4 name and age 2')
new_dict = {names: age for (names, age) in zip(name, age)}
print(new_dict)

# Si realizo de esta forma la creación del diccionario lo que va a hacer el programa es asociarme todas las canciones con los 5 artistas, y lo que quiero es que cada uno tenga la suya

print('')
print('Examples')
artist = ['ACDC', 'Metallica', 'Abba', 'Muse', 'MJ']
songs = ['XXXX', 'YYYY', 'ZZZZ', 'Do not hear it', 'best one']
music = {}
for art in artist:
  music[art] = {song for song in songs}
print(music)

# En este caso me creo una lista, no un diccionario, con las combinaciones que quiero

print('')
artist = ['ACDC', 'Metallica', 'Abba', 'Muse', 'MJ']
songs = ['XXXX', 'YYYY', 'ZZZZ', 'Do not hear it', 'best one']
music = list(zip(artist, songs))
print(music)

# Ya me creo el diccionario con la combinación que se realizó con anterioridad

print('')
artist = ['ACDC', 'Metallica', 'Abba', 'Muse', 'MJ']
songs = ['XXXX', 'YYYY', 'ZZZZ', 'Do not hear it', 'best one']
music = dict(list(zip(artist, songs)))
print(music)

# Aca con un simple for pude combinar ambas listas y crear un diccionario, usando zip

for (art, song) in zip(artist, songs):
  music[art] = song
print(music)