'''
Clusters (sets) can be modified, it doesn't have a specific order, and it doesn't allow duplicates (if in the declaration I include the duplicate, it is going to omit it). They can be misunderstood from being a dictionary, but if it doesn't have a key, it uses {} and is like a list. It allows varios types of variables, like a number, text, decimales, and more

If I'm going to use a string, the result is that the set will divide the word into the letters and will create an order 

If I want to know if there is a numbers written down more han 2 times in a list? Convert it into a set 
'''

countries_set = {'col', 'usa', 'mex'}
print(countries_set)
print(type(countries_set))

numbers_set = {1,2,3,4,5,5}
print(numbers_set)
print(type(numbers_set))

types_set = {1, 'mex', 2.2, False, True}
print(types_set)
print(type(types_set))

strings_set = set('hello')
print(strings_set)
print(type(strings_set))

tuple_set = set(('adb', 'dc', 'abc', 'abc'))

# Se eliminan los duplicacos en los sets, simplemente se filtra la información

numbers = [1, 2, 3, 4, 5, 5, 5, 6, 1, 2, 3, 7, 8]
print(numbers)
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)