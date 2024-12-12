con = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
char = []


for i in range(10):
    letra = str(input('Digite 10 caracteres do alfabeto: '))
    if letra in con:
        char.append(letra)
    else:
        continue

print(char)