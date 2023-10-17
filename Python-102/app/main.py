import utils
import read_csv
import charts
import pandas as pd


def run():

  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  labels = list(map(lambda y: y['Country/Territory'], data))
  values = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(labels, values)
  '''

  # The previous document reading is easier with pandas as follows:

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages) 
  
  data = read_csv.read_csv('data.csv')
  country = input('type country ')
  print(country)
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    
if __name__ == '__main__':
  run()

'''
import read_csv

def run():
  data = read_csv.read_csv('./app2/data.csv')
  data = list(lambda item: item['Continent'] == 'South America', data)

  countries = list(lambda y: y['Country/Territory'], data)
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  print(countries)

if __name__ == '__main__':
  run()
'''


'''
Pasos
La data se obtiene desde el diccionario en read_csv, que es el nombre del modulos y se usa un . para determinar la función. Luego se pasa directamente donde está el archivo con ./app/data.csv
Luego hay que seleccionar el país que queremos usar, con el input se puede escribir
El util me ayuda a seleccionar el país en el diccionario
Aca llega el resultado que debe ser mayor a 0 porque es un país encontrado
Se usa result[0], porque se supone que es de donde va a arrancar de nuevo el programa a filtrar los datos en una lista
Con el nombre del país se pasa a filtrar su información de población por año en la función get_population que esta en el modilo utils
Ya había definido en utils los keys y labels, que debo poner en la función de bar chart que esta en charts
'''