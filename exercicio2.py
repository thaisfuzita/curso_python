nome = 'Maria Helena'

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[1])
contador = 0 
novo_nome = '*'

while contador < len(nome):
    letra = f'{nome[contador]}*'
    novo_nome += letra
    contador += 1

print(novo_nome)
    