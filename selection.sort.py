import random

tamanho = 15
array = [random.randint(1, 100) for _ in range(tamanho)]

print("Array original:")
print(array)

for i in range(len(array)):
    valor = i
    
    for j in range(i + 1, len(array)):

        if array[valor] > array[j]:
            valor = j
    
    array[i], array[valor] = array[valor], array[i]

print("Array ordenado:")
print(array)