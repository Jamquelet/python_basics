#sacar una conclucion de una lista, trasformar una lista a un solo valor, toca importarlo
import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item:counter + item, numbers ) #recibe dos variables una q va incrementando el valor y la otra es el item que vamos a estar iterando, luego le damos la lista que vamos a iterar
print(result)#10

#
def accum(counter, item):
    print('counter =>', counter)
    print('item =>', item)
    return counter + item
result2 = functools.reduce(accum, numbers )
print(result2)

# Iteration - Counter - Item - Return 
# 1         - 0       - 1    - 1
# 2         - 1       - 2    - 3
# 3         - 3       - 3    - 6
# 4         - 6       - 4    - 10

import functools
numbers2 = [1, 2, 3, 4, 5]
result2 = functools.reduce(lambda a, b: a + b, numbers2)
print(result2)

#
from functools import reduce
print(reduce( lambda a, b: a+b, [1, 2, 3, 4])) #10

assert reduce( lambda a, b: a+b, [1, 2, 3, 4]) == sum([1,2,3,4])

#calcular el factorial de n
from functools import reduce
reduce(lambda x, y: x * y, range(1,5))

