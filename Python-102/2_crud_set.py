countries_set = {'col', 'usa', 'mex'}

size = len(countries_set)

print(size)
print('col' in countries_set)
print('per' in countries_set)

# Add elements to the set

countries_set.add('per')
print(countries_set)

'''
Even if I add more elements that are the same, python is going to still show me only one
'''

# Update, also enables python to add more elements

countries_set.update({'per', 'ecu', 'arg', 'bol'})
print(countries_set)

# Remove elements

countries_set.remove('usa')
print(countries_set)
'''
If the element that I'm looking for doesn't exits, lets say is 'ar' and we are removing 'arg', python is going to show an error. But we can use discard, so an error doesn't appear
'''
countries_set.discard('arg')
print(countries_set)
countries_set.clear()
print(countries_set)
print(len(countries_set))