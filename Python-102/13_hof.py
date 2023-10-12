def function(x):
  return x + 1

def other_function(x, func):
  return 2 * x + func(x)

result = other_function(2, function)
print(result)

# Same version with lambdas

increment = lambda x: x + 1
other_func = lambda x, func: 2 * x + func(x)

result_v2 = other_func(3, increment)
print(result_v2)

result_v3 = other_func(3, lambda x: x * 2)
print(result_v3)
result_v4 = other_func(3, lambda x: x * 5)
print(result_v4)