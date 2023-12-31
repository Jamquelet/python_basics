#aplica una funcion a cada elemento del iterable, es perezoso
#transformacion de elementos
numbers=[1,2,3,4]
numbers_v2=[]

for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)


numbers_v3 =list(map(lambda i: i*2, numbers))
print(numbers_v3)
print(numbers)
numbers2=[1,2,3,4]
numbers3=[5,6,7]

result = list(map(lambda x,y:x+y, numbers2,numbers3))# [6,8,10] dado el tamaño de la lista omite el 4 al no tener con q sumarlo
print(result)

#diccionarios

items=[
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalon',
        'price': 200
    },
    {
        'product': 'hat',
        'price': 500
    }]
prices=list(map(lambda item: item['price'],items))
print(prices)


def add_taxes(item):
    item['taxes']=item['price']*.19
    return item

new_items = list(map(add_taxes,items)) #modifica el array original
print(new_items)


def multiply_numbers(numbers):
    result = list(map(lambda x: x*2, numbers))
    return result

numbers = [1,2,3,4]
response = multiply_numbers(numbers)
print(response)

#con un ciclo for 

def multiply_numbers2(numbers):
    numbers2 = []
    for x in numbers:
        numbers2.append(x*2)
    return numbers2

numbers = [1,2,3,4]
response = multiply_numbers2(numbers)
print(response)

#
def cuadrado(n: int):
    return n**2
l=[1,2,3,4,5,6]

cuadrados_1 = [cuadrado(n) for n in l]
print(cuadrados_1)

for c in map(cuadrado, l):
    print(c)

cuadrados_2 = list(map(cuadrado, l))
print(cuadrados_2)

list(map(int, input().split()))