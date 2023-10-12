# Aca le estoy diciendo al programa, vea use la información en data y busque el país que quiero tener especificamente. Por eso, data y country son las variables de entrada de poplation_by_country

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

# En este caso, me toca revisar y estar atento a que es lo que dice el header, porque no dice Country solo, sino Country/Territory. Tenía el codigo perfecto, pero solo porque no tenía bien el nombre no función


# La idea de utils es traer la información que necesitamos para graficar, obteniendo la población. Se supone que con country_dict ya está entrando el diccionario del país de donde quiero sacar la info. Se pregunta por la columna tal cual como está en el archivo '2022 Population'...

'''
def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  # Para poder hacer las gráficas se necesita mandar los labels (parametros) y values (numeros)
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values
'''