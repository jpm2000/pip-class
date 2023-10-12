import sys
print(sys.path)

import re
text = 'My phone number is 123456789, and I am watching the 90th game, where 50 people are playing and I just had my 20th pizza' 
result = re.findall("['0-9']+", text)
print('')
print(result)

import time
timestamp = time.time()
print('')
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print('')
print(result)

import collections
numbers = [1,1,2,3,1,2,2,1,4,1,4,5,100]
counter = collections.Counter(numbers)
print('')
print(counter)