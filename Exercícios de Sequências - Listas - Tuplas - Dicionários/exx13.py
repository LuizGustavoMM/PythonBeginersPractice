meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", 
    "Maio", "Junho", "Julho", "Agosto", 
    "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
temperatura_meses = []
cont = 0

for mes in meses:
    temp = float(input(f'Informe a temperatura média do mês {mes}:'))
    temperatura_meses.append(temp)

temp_media = (sum(temperatura_meses))/12

print(f'\nMédia anual de temperatura: {temp_media:.0f}°C\n')
print('Meses com temperatura a cima da média anual: ')

for indice, temp in enumerate(temperatura_meses):
    if temp > temp_media:
        cont += 1
        print(f'{cont} - {meses[indice]}: {temp:.0f}')