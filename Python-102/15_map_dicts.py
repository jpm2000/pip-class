items = [
  {
    'product' : 'shirt',
    'price' : 100,
  }, 
  {
    'product' : 'jeans',
    'price' : 200
  },
  {
    'product' : 'shoes',
    'price' : 500
  }
]

prices = list(map(lambda item : item['price'], items))
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * 0.19 
  return item

new_items = list(map(add_taxes, items))
print(new_items)

def add_size(item):
  item['size'] = 'S', 'M', 'L'
  return item

new_items_2 = list(map(add_size, items))
print(new_items_2)

print('')

'''
variable = list(map(lambda var : var['product'], items))
print(variable)

def add_size_v2(var):
  if var == 'shirt':
    var['size_2'] = 'S', 'M', 'L'
  elif var == 'jeans':
    var['size_2'] = '28', '30', '32', '34'
  elif var == 'shoes':
    var['size_2'] = '38', '39', '40', '41', '42'
  return var

new_items_3 = list(map(add_size_v2, items))
print(new_items_3)
'''

variable = list(map(lambda var : var['product'], items))
print(variable)

def add_size_v2(var):
  var['size_2'] = 'S', 'M', 'L'
  var['size_2'] = '28', '30', '32', '34'
  var['size_2'] = '38', '39', '40', '41', '42'
  return var

new_items_3 = list(map(add_size_v2, items))
print(new_items_3)