import random

def bubbleSort(array):
    
    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = var

tamanho = 15
array = [random.randint(1, 100) for _ in range(tamanho)]

print("Array original:")
print(array)

bubbleSort(array)

print("Array ordenado:")
print(array)
