# operadores artiméticos
# +, - , /, *
nota1 = 3.0
nota2 = 5.5
media = (nota1 + nota2)/2

#2 elevado ao quadrado
potencia = 2 ** 2

numero = 2 * 2 * 2

#operadores de atribuição
# =, +=, -=, .....

idade = 20

#idade = idade + 10
idade += 10

#operadores lógicos
# and, or ,not

print(True or True)

resultado = True and False
print(resultado)

# and
# 1 1 = 1
# 1 0 = 0 
# 0 1 = 0
# 0 0 = 0

# or
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0

# Operadores de comparação 
# ==, !=, >, <, >=, <=

idade = 17

if idade >= 18:
    print("Maior de Idade")
else:
    print("Menor de Idade")


# operador is
# os valores do obejto e se ocupam o mesmo espaço de memória

a = [1,2,3]
b = [1,2,3]    
print(a is b)

z = [1,2,3]
x = z
print(z is x)

# operador in e not in
# verificar se um objeto está ou não dentro de uma sequência (str, list, tuple, .....)

print("a" in "Java")
print("Maria" in ["Pedro", "Ana"])
print("Maria" not in ["Pedro", "Ana"])