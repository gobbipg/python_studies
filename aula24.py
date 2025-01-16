# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# O t a v i o
# -6-5-4-3-2-1

# nome = 'PAULO'

# print(nome [2])
# print(nome [0])
# print(nome [-2])
# print('ULO' in nome)
# print('GOB' in nome)
# print(10 * '-')
# print('ULO' not in nome)
# print('GOB' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está dentro do {nome}')

else:
    print(f'{encontrar} não está em {nome}')