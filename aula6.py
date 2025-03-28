palavra = 'debora'
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
i = 1
letras_acertadas = ''
repeticoes = 0

import os

while True:
    chute = input('Digite uma letra: ')
    repeticoes += 1

    if len(chute) > i:
        print('Digite apenas uma letra')
        continue

    elif chute not in alfabeto:
        print('Letra inválida')
        continue

    elif chute in palavra:
        letras_acertadas += chute
    
    palavra_formada = ''
    for x in palavra:
        if x in letras_acertadas:
            palavra_formada += x
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('VOCÊ GANHOU! PARABÉNS')
        print('A palavra era', palavra)
        print('Tentativas:', repeticoes)
