'''
There are different types of scopes within python, for example global or local scopes. This means that if I put the name of a variable multiple times in different scope, is not going to be the same variable, it will depend on the scope
'''

# Global scope
price = 100 

print(price)

# A new context or scope
def increment():
  price = 200
  #If I use result instead of price and try to print it outside the scope it wont work
  price = price + 100
  print(price)
  return price

price_2 = increment()
print(price_2)