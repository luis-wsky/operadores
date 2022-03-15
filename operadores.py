# operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.
# 5+2 ==  5-2==  5*2==  5/2== 5**2== elevado  5//2== divisão inteira 5%2==resto da divisão
nome = str(input('Qual e o seu nome?'))
print('Legal!, {:=^20}, vamos para os cálculos?'.format(nome))
n1 = float(input('Digite um número'))
n2 = float(input('Digite outro número'))
soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
potencia = n1**n2
antecessor = n1 - 1
sucessor = n1 + 2
print('A soma é {}'.format(soma))
print('A subtração é {}'.format(subtracao))
print('A multiplicação é {}'.format(multiplicacao))
print('A divisão é {}'.format(divisao))
print('A potência é {}'.format(potencia))
print('Acabou, quer mais?')
print('O antecessor do primeiro número digitado é {}'.format(antecessor))
print('O sucessor do primeiro número digitado é {}'.format(sucessor))
