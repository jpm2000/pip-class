'''
I can use the following to be more specific on what I want to run
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4


print(func_1())
print(func_2())
print(func_3())
print(func_4())

The package is a way to organize multiple modules
'''

import pkg
print(pkg.URL)

# No es muy practico, porque ya arriba mande los modulos. Hay que hacer la importación explicita, se puede hacer desde pkg
print(pkg.mod_1.func_1())
print(pkg.mod_1.func_100())
print(pkg.mod_2.func_1000())