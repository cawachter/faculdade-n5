with open('texto.txt', 'w') as f:

    texto = list()

    texto.append("Oi, esta é a primeira linha do meu novo arquivo criado com python!")
    texto.append("E agora temos uma segunda linha.")
    texto.append("Olha que legal, coloquei uma terceira linha.")


    for i in texto:
        f.write(i + '\n')

