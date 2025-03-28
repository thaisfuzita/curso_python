import random

def decimal_para_complemento_2(numero, bits=8):
    if numero >= 0:
        binario = bin(numero)[2:].zfill(bits)  # Conversão direta
    else:
        binario = bin((1 << bits) + numero)[2:]  # Complemento de 2
    return binario

def complemento_2_para_decimal(binario):
    bits = len(binario)
    if binario[0] == '0':
        return int(binario, 2)  # Número positivo
    else:
        return int(binario, 2) - (1 << bits)  # Conversão de complemento de 2

def jogo():
    print("Bem-vindo ao jogo do Complemento de 2!")
    print("Converta corretamente os números para ganhar pontos.")

    pontuacao = 0
    tentativas = 5

    for _ in range(tentativas):
        numero = random.randint(-10, 10)  # Gera um número aleatório
        bits = 8  # Tamanho fixo de 8 bits

        if random.choice([True, False]):
            # Pergunta de decimal para complemento de 2
            print(f"Qual a representação em complemento de 2 do número {numero} em {bits} bits?")
            resposta = input("Resposta: ")
            resposta_correta = decimal_para_complemento_2(numero, bits)
        else:
            # Pergunta de complemento de 2 para decimal
            resposta_correta = decimal_para_complemento_2(numero, bits)
            print(f"Qual o valor decimal do número binário {resposta_correta}?")
            resposta = input("Resposta: ")
            resposta_correta = str(complemento_2_para_decimal(resposta_correta))

        if resposta == resposta_correta:
            print("Correto! +1 ponto")
            pontuacao += 1
        else:
            print(f"Errado! A resposta correta era {resposta_correta}")

    print(f"Jogo encerrado! Sua pontuação final: {pontuacao}/{tentativas}")

if __name__ == "__main__":
    jogo()
