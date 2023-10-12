numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

numbers_v3 = list(map(lambda x: x * 5, numbers))
print(numbers_v3)

num_1 = [1, 2, 3, 4, 5]
num_2 = [7, 8, 9]

result = list(map(lambda x, y: x + y, num_1, num_2))
print(result)