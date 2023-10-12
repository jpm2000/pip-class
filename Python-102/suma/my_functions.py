info = [
  {
    'customerName': "Nicolas",
    'total': 100,
    'delivered': True
  },
  {
    'customerName': "Zulema",
    'total': 120,
    'delivered': False
  },
  {
    'customerName': "Santiago",
    'total': 20,
    'delivered': False
  }
]

name = input('write a name ')

def ordenes(info, name):
  result = list(filter(lambda cli : cli['customerName'] == name, info))
  return result

print(result)