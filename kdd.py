palavras = list()
with open('texto.txt', 'r') as file:
    for linha in file:
        palavras_na_linha = linha.split()
        palavras.extend(palavras_na_linha)

print("Palavras extraídas do arquivo:")
print(palavras)

import time

def bubble_sort(array):

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = var

def selection_sort(array):
    for i in range(len(array)):
        valor = i
    
        for j in range(i + 1, len(array)):

            if array[valor] > array[j]:
                valor = j
        
        array[i], array[valor] = array[valor], array[i]

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

bubble_sort(palavras)
bubble_time = measure_time(bubble_sort, palavras)
print("Ordenação usando Bubble Sort:")
print(palavras)
print(f"Tempo de execução (Bubble Sort): {bubble_time:.6f} segundos\n")

palavras = list()
with open('texto.txt', 'r') as file:
    for linha in file:
        palavras_na_linha = linha.split()
        palavras.extend(palavras_na_linha)

print("Palavras extraídas do arquivo:")
print(palavras)

selection_sort(palavras)
selection_time = measure_time(selection_sort, palavras)
print("Ordenação usando Selection Sort:")
print(palavras)
print(f"Tempo de execução (Selection Sort): {selection_time:.6f} segundos\n")

palavras = list()
with open('texto.txt', 'r') as file:
    for linha in file:
        palavras_na_linha = linha.split()
        palavras.extend(palavras_na_linha)

print("Palavras extraídas do arquivo:")
print(palavras)

palavras.sort()
sort_time = measure_time(lambda x: x.sort(), palavras)
print("Ordenação usando o método sort() nativo:")
print(palavras)
print(f"Tempo de execução (sort() nativo): {sort_time:.6f} segundos")

with open('ordenado.txt', 'w') as file:
    for palavra in palavras:
        file.write(palavra + '\n')

print("\nPalavras ordenadas foram escritas no arquivo 'ordenado.txt'.")
