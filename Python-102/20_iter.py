for i in range(1, 10):
  print(i)

my_iterable = iter(range(1, 11))
print(my_iterable)

# en el for se realiza la iteración, por fuera no. Pero si le pongo la funcion iter(), se ve raro pero es un iterable. Con esto, se pueden realizar iteraciones manuales

print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))

# Por cada next tengo el iterable, va generando progresivamente. Es importante para ver los archivos, a veces nos toca tener manualmente la iteración, sin un for. Si ya se llegó hasta el punto en el que se puede iterar, va a generar un error y me dirá stop iteration
