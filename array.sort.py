import random

tamanho = 15
array1 = [random.randint(1, 100) for _ in range(tamanho)]
array2 = ["nome", "dataNascimento", "cpf", "rg"]

print("Array1 original: ")
print(array1)

print("Array2 original: ")
print(array2)

array1.sort()
array2.sort()

print("Array1 ordenado:")
print(array1)

print("Array2 ordenado:")
print(array2)

array1.sort(key=None, reverse=True)
array2.sort(key=None, reverse=True)

print("Array1 ordenado em ordem decrescente:")
print(array1)

print("Array2 ordenado em ordem decrescente:")
print(array2)