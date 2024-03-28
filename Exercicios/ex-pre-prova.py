#Ex-01
import random
def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    rodada = 1
    tentativas_restantes = 10
    while rodada <= 10:
        palpite = int(input(f'Rodada {rodada}; Digite seu palpite (1 a 100): '))

        if palpite < 1 or palpite > 100:
            print(f'Palpite inválido; Digite apenas um número entre 1 e 100.\n')
            continue

        if palpite > numero_secreto:
            print(f'Palpite alto; Tentativas restantes: {tentativas_restantes - 1}\n')
            tentativas_restantes -= 1
        elif palpite < numero_secreto:
            print(f'Palpite baixo; Tentativas restantes: {tentativas_restantes - 1}\n')
            tentativas_restantes -= 1
        else:
            print(f'PARABÉNS! Você adivinhou o número secreto ({numero_secreto}) na rodada {rodada}.'
                  f'\nVocê gastou {10 - tentativas_restantes} tentativas.\n')
            break

        if rodada == 10 and palpite != numero_secreto:
            print(f'Game Over! Você não acertou o número secreto ({numero_secreto}).'
                  f' Tente novamente!')

        rodada += 1

if __name__ == '__main__':
    jogar_adivinhacao()
#Ex-02
def exibir_tabuada():
    numero = int(input('Digite um número: '))
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i:2} = {resultado:2}')

if __name__ == '__main__':
    exibir_tabuada()
#Ex-03
def vogais_e_consoantes(frase):
    vogais = 'aeiou'
    consoantes = ''
    for letra in frase:
        if letra.lower() in vogais:
            vogais_count += 1
        elif letra != ' ':
            consoantes += letra

    consoantes_count = len(consoantes)
    return vogais_count, consoantes_count

def main():
    frase = input('Digite uma frase: ').strip()
    vogais, consoantes = vogais_e_consoantes(frase)
    print(f'O número de vogais é: {vogais}\nO número de consoantes é: {consoantes}')

if __name__ == '__main__':
    main()
    #Ex-04