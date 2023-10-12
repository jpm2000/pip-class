def find_volume(height=1, length=1, width=1):
  print(height, length, width)
  return height * length * width, width, 'Hello'

result = find_volume(20,30,40)
length = find_volume(length=20)
text = find_volume()
print(result)
print(length)
print(text)

result, length, text = find_volume(1,2,3)
print
print(result)
print(length)
print(text)

print('')

def math_prob(a=1, b=2, c=3, d=4, e=5):
  cal = ((a * b) / c) + d - e
  return cal, a, b, c, d, e, 'just calculated some random numbers'

result, a, b, c, d, e, text = math_prob(10, 20, 4, 3, 1)
print(result)
print(a)
print(b)
print(c)
print(d)
print(e)
print(text)

print('')

result, a, b, c, d, e, text = math_prob(b=30, e=50)
print(result)
print(a)
print(b)
print(c)
print(d)
print(e)
print(text)