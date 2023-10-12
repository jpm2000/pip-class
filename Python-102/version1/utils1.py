def get():
  keys = ['col', 'bol']
  values = [50, 30]
  return keys, values



'''
Normalmente este tipo de modulos tiene funciones (def)
'''


def pais(info, country):
  result = list(filter(lambda item : item['Country'] == country, info))
  return result

