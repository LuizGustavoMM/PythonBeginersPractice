sexo = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Sexo inválido!')
    sexo = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]
print('Resposta registrada!')