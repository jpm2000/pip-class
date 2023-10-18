import matplotlib.pyplot as plt
import utils

# ax son las coordinadas donde vamos a graficar
'''
def generate_bar_chart():
  labels = ['a', 'b', 'c']
  values = [100, 200, 300]
  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  generate_bar_chart()
'''

#Con esto reconoce que es un script, ayuda a que se ejecute bien como un archivo
'''
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  labels = utils.population_by_country(labels)
  values = utils.population_by_country(values)
  generate_bar_chart(labels, values)
'''



# .show ayuda a que el output siga corriendo y mostrando la ejecución

'''
  labels = utils.population_by_country(labels)
  values = utils.population_by_country(values)

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 2000, 300]
  generate_pie_chart(labels, values)

'''

# Proyecto

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('chart_pie_final.png')
  plt.close()


if __name__ == '__main__':
  #labels = utils.population_by_country(labels)
  #values = utils.population_by_country(values)
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)