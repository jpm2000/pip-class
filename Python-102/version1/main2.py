import utils1

info = [
  {
    'Country': 'Colombia',
    'Population': 50
  },
  {
    'Country': 'Bolivia',
    'Population': 30
  }
]

def run():
  keys, values = utils1.get()
  print(keys, values)
  
  country = input('type the country -> ')
  
  result = utils1.pais(info, 'Colombia')
  print(result)


# dualidad
if __name__ == '__main__':
  run()

'''
What I want with the lines of code down, is that even if I want to run the code from main2 I can do it. I don't have to rely on doing it in example.
If I'm not running the code in other modules and I want to use the code
Dualidad is that I can use the code in the terminal and any modules
'''