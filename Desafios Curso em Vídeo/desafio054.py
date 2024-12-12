from datetime import date
print('Digite 7 anos de nascimento e saiba quantos são maiores e quantos não são.')
tot = 0
at = date.today().year
for c in range(1, 8):
   ano = int((input('Digite o {}° ano: ' .format(c))))
   if at - ano >= 18:
       tot += 1
print('Dessas 7 pessoas {} tem maioridade.' .format(tot))
print('Dessas 7 pessoas {} são menores de idade.' .format(7-tot))