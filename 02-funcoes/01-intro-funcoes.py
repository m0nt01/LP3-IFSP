# Função 
# modulariar o programa
# reuso
# manutenabilidade

# só pode acessar hora estiver entre 8h e 18h
hora_atual = 12
if hora_atual >= 8 and hora_atual <= 18:
    print('permitido o acesso')

# entrada = hora_atual
# saida se está dentro ou não do horário comercial
def dentro_do_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

# Declaração
# def nome_ funcao():
#    corpo da funcao

# Função sem retorno
# side effect - efeito colateral
def diga_ola(nome):
    print(f'Olá {nome}')

# Chamada
diga_ola = ('Marcos')

# Função com retorno
# Sem side effect = função pura
def montar_frase(nome):
    return f'Olá {nome}'
nome = 'ZéDaManga'
print(montar_frase(nome))

# Parâmetro e Argumentos
# Parâmetro são referencias que podem ser acessadas
# dentro da função
# Argumento são os valores passados para os parâmetros
def somar(numero1, numero2):
    return numero1 + numero2

somar(10.0, 5.0)

# Escopo de variáveis
# Variável local
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

#print(media)

# Variável global
total = 0.0

def soma(n1, n2, n3):
    # global total
    total = n1 + n2 + n3
    return total
print(total)
soma(1, 3, 5)
print(total)

# Parâmetros com valor padrão
def boas_vindas(nome, mensagem = 'Buogiorno'):
    return f"{mensagem}, {nome}"
print(boas_vindas('Bom dia', 'Marcos'))
print(boas_vindas('Maria'))

# Argumentos nomeados
print(boas_vindas(nome = 'Maria'))

# DocString
# comentário de documentação
def somar(n1 ,n2):
    '''
    função que soma dois números
    :para n1: primeiro número
    :para n2: segundo número
    :return: soma dos números
    '''
    return n1 + n2
# Funções built-in
# print, type, len, sum, max, min, input

print('sdadsahdshad')