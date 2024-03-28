#Ex-01
num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1
print(f'O número {num} tem esse antecessor {antecessor} e o sucessor {sucessor}')

#Ex-02
n1 = int(input('Digite 1 número: '))
n2 = int(input('Digite 1 número: '))
n3 = int(input('Digite 1 número: '))
Sarit = n1 + n2 + n3 / 3
print(f'A soma Aritmetica dos números é: {Sarit}')

#Ex-03
valor_compra = float(input('Digite o valor da compra: R$ '))

if 0.01 <= valor_compra <= 9.99:
    desconto = 0.0  # 0% discount
    valor_final = valor_compra - (valor_compra * desconto)
    print(f'Valor final com desconto: R$ {valor_final:.2f}\nDesconto aplicado: {desconto:.2f}%')

elif 10.0 <= valor_compra <= 99.99:
    desconto = 0.05  # 5% discount
    valor_final = valor_compra - (valor_compra * desconto)
    print(f'Valor final com desconto: R$ {valor_final:.2f}\nDesconto aplicado: {desconto:.2f}%')

elif 100.0 <= valor_compra <= 499.99:
    desconto = 0.10  # 10% discount
    valor_final = valor_compra - (valor_compra * desconto)
    print(f'Valor final com desconto: R$ {valor_final:.2f}\nDesconto aplicado: {desconto:.2f}%')

elif valor_compra >= 500.0:
    desconto = 0.15  # 15% discount
    valor_final = valor_compra - (valor_compra * desconto)
    print(f'Valor final com desconto: R$ {valor_final:.2f}\nDesconto aplicado: {desconto:.2f}%')

else:
    print('Entrada inválida. Por favor, digite um valor válido para a compra.')
    #Ex-04
    def verificar_codigo_funcionario(identificador):
     if len(identificador) != 7:
        return False
     if not identificador.isalpha() and not identificador.isdigit():
        return False
     if identificador[:2] != 'BR':
        return False
     if not identificador[2:6].isdigit():
        return False
     if int(identificador[2:6]) < 1 or int(identificador[2:6]) > 9999:
        return False
     if identificador[6] != 'X':
        return False
     return True

    #Ex-05
    def is_valid_identificador(identificador):
     if len(identificador) != 7:
        return False
     if not identificador.isalpha() and not identificador.isdigit():
        return False
     if identificador[:2] != 'BR':
        return False
     if not identificador[2:6].isdigit():
        return False
     if int(identificador[2:6]) < 1 or int(identificador[2:6]) > 9999:
        return False
     if identificador[6] != 'X':
        return False
     return True

def main():
    identificador = input('Digite um identificador (7 caracteres, iniciando con "BR", contendo um número inteiro entre 0001 e 9999, e terminando com "X"): ')
    if is_valid_identificador(identificador):
        print('O identificador é válido.')
    else:
        print('O identificador é inválido.')

if __name__ == '__main__':
    main()
   #Ex-06
    def get_volume(comprimento, altura, largura):
     return (comprimento * altura * largura) / 1000

def get_heater_power(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def get_filtration_flow(volume):
    return volume * 2

def main():
    comprimento = float(input('Digite o comprimento do aquário em centímetros: '))
    altura = float(input('Digite a altura do aquário em centímetros: '))
    largura = float(input('Digite a largura do aquário em centímetros: '))

    temp_desejada = float(input('Digite a temperatura desejada para o aquário em graus Celsius: '))
    temp_ambiente = float(input('Digite a temperatura ambiente em graus Celsius: '))

    volume = get_volume(comprimento, altura, largura)
    print(f'Volume do aquário em litros: {volume:.2f} L')

    potencia = get_heater_power(volume, temp_desejada, temp_ambiente)
    print(f'Potência do termostato necessária: {potencia:.2f} Watts')

    filtragem_por_hora = get_filtration_flow(volume)
    print(f'Filtragem por hora necessária: {filtragem_por_hora:.2f} L/hora')

if __name__ == '__main__':
    main()
    #Ex-07
def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 18.5:
        classificacao = 'Baixo peso'
    elif 18.5 <= imc < 24.9:
        classificacao = 'Peso normal'
    elif 25.0 <= imc < 29.9:
        classificacao = 'Excesso de peso'
    elif 30.0 <= imc < 34.9:
        classificacao = 'Obesidade de Classe 1'
    elif 35.0 <= imc < 39.9:
        classificacao = 'Obesidade de Classe 2'
    else:
        classificacao = 'Obesidade de Classe 3'
    return classificacao

def recomendar_mudanca_peso(peso, classificacao, imc_referencia):
    if classificacao in ['Peso normal']:
        print('Seu IMC está normal. Parabéns!')
    else:
        diferenca = peso / (imc_referencia / (18.5 ** 2)) - peso
        if diferenca > 0:
            print(f'Seu IMC é de {classificacao}. Você deve perder {diferenca:.1f} Kg para atingir o peso normal.')
        else:
            print(f'Seu IMC é de {classificacao}. Você deve ganhar {abs(diferenca):.1f} Kg para atingir o peso normal.')

def principal():
    peso = float(input('Digite seu peso em quilogramas (Kg): '))
    altura = float(input('Digite sua altura em metros (m): '))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f'Classificação: {classificacao}\n')
    print('IMC = 24.9 é considerado peso normal.')
    recomendar_mudanca_peso(peso, classificacao, 24.9)

if __name__ == '__main__':
    principal()