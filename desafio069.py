contFem = contMas = contIdade = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite [M/F] para o sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('\nInsira as informações corretas!\n')
        sexo = str(input('Digite [M/F] para o sexo: ')).strip().upper()[0]

    if sexo in ('M'):
        contMas += 1
    
    if idade >= 18:
        contIdade += 1
    
    if sexo in ('F') and idade < 20:
        contFem += 1
    
    continuar = str(input('Deseja continuar? [S/N]\n\nR: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]\n\nR: ')).strip().upper()[0]

    if continuar == 'S':
        continue
    
    elif continuar == 'N':
        break
print(f'Pessoas com mais de 18 anos: {contIdade}')
print(f'Mulheres com menos de 20 anos: {contFem}')
print(f'Quantidade de homens cadastrados: {contMas}')