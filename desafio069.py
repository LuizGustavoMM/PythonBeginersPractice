contFem = 0
contMas = 0
contIdade = 0

while True:
    sexo = input('Digite [M/F] para o sexo: ')
    idade = int(input('Digite a idade: '))

    if sexo in ('Mm'):
        contMas += 1
    
    if idade >= 18:
        contIdade += 1
    
    if sexo in ('Ff') and idade < 20:
        contFem += 1
    
    else: 
        print('Insira as informações corretas.')
    
    continuar = input('Deseja continuar? [S/N]\n\nR: ')

    if continuar in ('Ss'):
        continue
    
    elif continuar in ('Nn'):
        break
print(f'Pessoas com mais de 18 anos: {contIdade}')
print(f'Mulheres com menos de 20 anos: {contFem}')
print(f'Quantidade de homens cadastrados: {contMas}')