'''
There is a way to create my own functions to optimize my code, and basically this means that I can create my own 'print()' functions and call those however I want to with the conditions that I also want. 

If I want to send variables to the function I just add the variable name in the def ()
'''

def my_print(a,b,c,d,e):
  print(a + b - c * d / e)
  print('this a mathematical distraction')

my_print(1, 100, 400, 30, 50)

print('')

def worst(text):
  print(text * 2)
  print('no idea what I did there')
worst('hello')

print('')

def other(x, y):
  worst(x + y)

other(1, 2)

print('')

def my_print(text):
  print('This is my print')
  print('This is my print 2')

my_print('try it out')

print('')

def other_print(text):
  print(text * 2)


other_print('Hola esta es una prueba ')

a = 10
b = 90

c = a + b

print('')

def sum(a, b):
  print('Just the sum')
  print(a + b)
  print('')
  print('with other_print')
  other_print(a + b)

sum(10, 100)
sum(100, 122)
sum(50, 5000)


