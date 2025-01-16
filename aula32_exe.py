"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# CORRIGIDO:
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')

else:
    print('Você não digitou um número inteiro')


# QUE EU FIZ:
numero_int = int(input('Digite um número inteiro: '))

verificacao = numero_int % 2

if verificacao == 0:
    print('O número é par.')

else:
    print('O número digitado é ímpar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# QUE EU FIZ / CORRIGIDO:
hora = input('Digite a hora em números inteiros: ')

try:

    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')

    elif hora >= 18 and hora <= 23:
        print('Boa noite!')

    else:
        print('Digite um número entre 0 e 23 horas.')

except ValueError:
    print('Entrada inválida. Por favor, digite um número.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# QUE EU FIZ:
nome = len(input('Digite seu primeiro nome: '))

if nome <= 4:
    print('Seu nome é curto!')

elif nome >= 5 and nome <= 6:
    print('Seu nome é normal!')

else:
    print('Seu nome é muito grande!')


# CORRIGIDO:
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:

    if tamanho_nome <= 4:
        print('Seu nome é curto.')

    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')

    else:
        print('Seu nome é grande.')

else:
    print('Digite mais de uma letra, por favor.')