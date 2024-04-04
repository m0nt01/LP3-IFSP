#Ex-01
import random
def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    rodada = 1
    tentativas_restantes = 10

    while rodada <= 10:
        palpite = int(input(f'Rodada {rodada}; Digite seu palpite (1 a 100): '))

        if not 1 <= palpite <= 100:
            print(f'Palpite inválido; Digite apenas um número entre 1 e 100.\n')
            continue

        if palpite > numero_secreto:
            print(f'Palpite alto; Tentativas restantes: {tentativas_restantes - 1}\n')
            tentativas_restantes -= 1
        elif palpite < numero_secreto:
            print(f'Palpite baixo; Tentativas restantes: {tentativas_restantes - 1}\n')
            tentativas_restantes -= 1
        else:
            print(f'PARABÉNS! Você adivinhou o número secreto ({numero_secreto}) na rodada {rodada}.\n'
                  f'Você gastou {10 - tentativas_restantes} tentativas.\n')
            break

        if rodada == 10 and palpite != numero_secreto:
            print(f'Game Over! Você não acertou o número secreto ({numero_secreto}).\n'
                  f'Tente novamente!')

        rodada += 1

if __name__ == '__main__':
    jogar_adivinhacao()

if __name__ == '__main__':
    jogar_adivinhacao()

#Ex-02
def exibir_tabuada():
    numero = int(input('Digite um número: '))

    for i in range(1, 11):
        print(f'{numero} x {i:02} = {numero * i:02}')

if __name__ == '__main__':
    exibir_tabuada()

#Ex-03
def vogais_e_consoantes(frase):
    vogais = 'aeiou'
    consoantes = ''
    contagem_vogais = [0] * len(vogais)
    contagem_consoantes = 0

    for letra in frase:
        if letra.islower():
            if letra in vogais:
                posicao = vogais.index(letra)
                contagem_vogais[posicao] += 1
            else:
                if letra != ' ':
                    consoantes += letra
                    contagem_consoantes += 1

    print(f'Vogais: {contagem_vogais}')
    print(f'Consoantes: {consoantes}\n' f'Total de consoantes: {contagem_consoantes}')

if __name__ == '__main__':
    frase = input('Digite uma frase: ')
    vogais_e_consoantes(frase)
    
    #Ex-04

candidatos = {'Candidato 1': 0, 'Candidato 2': 0, 'Candidato 3': 0}

votos = [0, 0, 0]

total_votos = 0

mensagem = "Digite o número do candidato que deseja votar, " \
          "caso deseje sair do programa digite 0: "

while True:
    if total_votos >= 10:
        break
    votos[input(mensagem)] += 1
    total_votos += 1


print("Resultado das eleições:")
print("Candidato 1: ", votos[0])
print("Candidato 2: ", votos[1])
print("Candidato 3: ", votos[2])

mais_votos = max(votos)

for i, voto in enumerate(votos):
    if voto == mais_votos:
        print("O candidato vencedor é Candidato ", i + 1, " com ", voto, " votos.")
    
    #Ex-05
palavra = input("Por favor, digite uma palavra ou frase: ")

if palavra == palavra[::-1]:
    print("A palavra/frase é um palíndromo!")
else:
    print("A palavra/frase não é um palíndromo.")
    #Ex-06
def converter_nota(pontuacao):
    if 90 <= pontuacao <= 100:
        return "A"
    elif 80 <= pontuacao < 90:
        return "B"
    elif 70 <= pontuacao < 80:
        return "C"
    elif 60 <= pontuacao < 70:
        return "D"
    else:
        return "F"

print("Conversor de Notas Escolares")
pontuacao = float(input("Digite a pontuação: "))
nota = converter_nota(pontuacao)
print("A nota correspondente é: ", nota)    

#Ex-07
def jogo_forca(): 
  palavra_oculta = 'python'
  total_tentativas = len(palavra_oculta) - 1

  while True:
    palavra_mostrada = ['_'] * len(palavra_oculta)
    for i, letra in enumerate(palavra_oculta):
      if letra in letras_descobertas:
        palavra_mostrada[i] = letra

    if '_' not in palavra_mostrada:
      print('Parabéns! Você descobriu a palavra oculta.')
      break

    letra_usuario = input('Adivinhe uma letra: ').lower()

    if letra_usuario in letras_descobertas:
      print('Você já tentou esta letra.')
      continue

 
    descoberta = False
    for i, letra in enumerate(palavra_oculta):
      if letra == letra_usuario:
        descoberta = True
        palavra_mostrada[i] = letra
        letras_descobertas.append(letra_usuario)

    if not descoberta:
      total_tentativas -= 1

    if total_tentativas == 0:
      print('Você perdeu!')
      print('A palavra oculta era:', palavra_oculta)
      break

    print('Palavra mostrada:', ''.join(palavra_mostrada))

letras_descobertas = []

jogo_forca()

#Ex-08
def count_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = input("Digite um texto: ")
word_count_dict = count_words(text)

print("\nDicionário de contagem de palavras:")
for word, count in word_count_dict.items():
    print(f"{word}: {count}")
    