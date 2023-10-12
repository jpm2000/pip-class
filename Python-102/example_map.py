'''
Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada
'''
numbers = [1, 2, 3, 4]

multiply_numbers = list(map(lambda x : x * 2, numbers))

print(multiply_numbers)
