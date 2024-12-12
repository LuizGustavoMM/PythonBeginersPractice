frase = str(input('Escreva uma frase: ')).strip().upper()
print('Quantos a tem: ', frase.count('A'))
print('O primeiro a da frase se encontra na posição: ', frase.find('A')+1)
print('O ultimo a da frase se encontra na posição: ', frase.rfind('A')+1)
