def increment(x):
  return x + 1

result = increment(10)
print(result)

increment_2 = lambda x : x + 1
result = increment_2(20)
print(result)

name = lambda name, last_name: f'Your name is {name.title()} {last_name.title()}'
your_name = name('juan pablo', 'manrique bonilla')
print(your_name)

print('')
print('Examples')


result = lambda age: age * 100
print(result(30))

