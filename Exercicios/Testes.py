import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    rodada = 1
    tentativas_restantes = 10

    while rodada <= 10:
        palpite = int(input(f'Rodada {rodada}; Digite seu palpite (1 a 100): '))
        if 1 <= palpite <= 100:
            if palpite > numero_secreto:
                print(f'Palpite alto; Tentativas restantes: {tentativas_restantes - 1}')
                tentativas_restantes -= 1
            elif palpite < numero_secreto:
                print(f'Palpite baixo; Tentativas restantes: {tentativas_restantes - 1}')
                tentativas_restantes -= 1
            else:
                print(f'PARABÉNS! Você adivinhou o número secreto ({numero_secreto}) na rodada {rodada}.')
                print(f'Você gastou {10 - tentativas_restantes} tentativas.')
                return
        else:
            print(f'Palpite inválido; Digite apenas um número entre 1 e 100.\n')

        if rodada == 10 and palpite != numero_secreto:
            print(f'Game Over! Você não acertou o número secreto ({numero_secreto}).')
            print(f'Tente novamente!')

        rodada += 1

if __name__ == '__main__':
    jogar_adivinhacao()