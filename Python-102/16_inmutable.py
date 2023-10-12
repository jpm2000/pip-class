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
  new = item.copy()
  new['taxes'] = new['price'] * 0.19 
  return new

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)

# the old list suffered the same modification that was made in the new list, there is a memory reference. If I create a copy and a new 'item' it won't change the original list
print('Old list')
print(items)


'''
def add_taxes(item):
  item['taxes'] = item['price'] * 0.19 
  return item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
'''
