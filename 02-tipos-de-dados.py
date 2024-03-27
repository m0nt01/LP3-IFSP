# Tipos de dados

# Numérico

# int
idade = 10

# float
altura = 1.65

# Booleano
# True, False
verdade = True
mentira = False
ligado = True
frete_gratis = True


# str = String
# sequência de caracteres
# literal de str
nome = "José"
nome = 'José'

# char
letra = "a"

frase = """
Olá pessoal
eu sou o Dollynho
seu amiguinho
vamos brincar?
"""

# Interpolação de string
nome = "Sonia"
idade = 23

# f-string
mensagem = f"Bom dia {nome}. Você tem {idade} anos!"

nome = "Silvio Santos"
print(nome[0:3])

# str são objetos
# métodos
print(nome.upper())
print(nome)

# list
# lista de valores
# pode conter valores de tipos diferentes
# podem ser alteradas (adicionar, remover)
habilidades = ['java', 'html', 'css']
print(habilidades[0])

habilidades[0] = 'javascript'
print(habilidades)

# adicionar no final
habilidades.append("python")
print(habilidades)

# adicionar em uma posição
habilidades.insert(0, 'kotlin')
print(habilidades)

# remove, sort, clear, copy,

for habilidade in habilidades:
    print(habilidade)


# tuple
# lista de valores
# não pode alterar os valores
opcoes = ('sim', 'não', 'talvez')
racas_rpg = ('anao', 'humano', 'elfo')

print(opcoes[1])
# funcao que retorna estatísticas
# sobre as notas de um aluno/aluna
# media , menor nota, maior nota
# entrada: n1, n2, n3 ou notas (list)
# saída: média, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas) / len(notas)
    menor = min(notas)
    maior = max(notas)
    return media, menor, maior


notas = [10.0, 5.5, 3.2, 1.8]
estatistica = estatistica_nota(notas)
print(estatistica)
print(type(estatistica))

# desempacotamento de tupla
media, menor, maior = estatistica_nota(notas)
print(media, menor, maior, True, 1.2) 

# set
# conjunto de valores
# não permite duplicados
# não é indexado
habilidades = {'java', 'python', 'css'}
habilidades.add('java')
print(habilidades)

# dict
# dicionario
# palavras
# palavra => definição
# chave => valor
# key => value
nome = "Silvio Santos"
casado = True
idade = 120

pessoa = {
    "nome": "SIlvio Santos",
    "casado": True,
    "idade": 120
}

print(pessoa["nome"])
print(pessoa["casado"])
print(pessoa["idade"])

pessoa["rico"] = True
print(pessoa)

# None
# null
nulo = None
