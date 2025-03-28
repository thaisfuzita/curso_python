numero = input('Digite um número inteiro: ')

try:
    if int(numero) % 2 == 0: 
        print('Este número é par')
    else: 
        print('Este número é ímpar')
except: 
    print('Este não é um número inteiro')

print(10 * '-')

hora = input('Digite o horário atual: ')
try:
    if int(hora) >= 0 and int(hora) <=11:
        print('Bom Dia')
    elif int(hora) >=12 and int(hora) <=17:
        print('Boa tarde')
    elif int(hora) >= 18 and int(hora) <=23:
        print('Boa noite')
    else:
        print('Horário inválido')
except:
    print('Horário inválido')

print(10 * '-')

nome = input('Digite seu nome: ')

if len(nome) > 1:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')