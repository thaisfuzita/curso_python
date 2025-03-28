nome = 'Thaís'
sobrenome = 'Fuzita'
idade = 27
ano_nascimento = 2025 - idade 
mes_de_nascimento = 9
maior_de_idade = idade >= 18
altura_metros = 1.63
peso = 60
imc = peso / (altura_metros)**2
print('nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?:', maior_de_idade)
print('Altura em metros:', altura_metros)
print('IMC:', imc)

print(nome, 'tem', altura_metros, 'de altura')
print('pesa', peso, 'quilos e seu imc é aproximadamente', int(imc))

linha_1 = f'{nome} tem {altura_metros:.1f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
print(linha_1)
print(linha_2)