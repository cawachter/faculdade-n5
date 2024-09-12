
with open('loremipsum.txt', 'r') as f:
    conteudo = f.read()

print("Conteúdo completo do arquivo:")
print(conteudo)

with open('loremipsum.txt', 'r') as f:
    primeira_linha = f.readline()

print("Primeira linha do arquivo:")
print(primeira_linha)

with open('loremipsum.txt', 'r') as f:
    tres_primeiros_caracteres = f.read(3)

print("Os 3 primeiros caracteres do arquivo:")
print(tres_primeiros_caracteres)

with open('loremipsum.txt', 'r') as f:
    conteudo_novo = f.read()

print("Conteúdo do arquivo lido novamente:")
print(conteudo_novo)

