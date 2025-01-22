"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Paulo', 'Anne', 'Luiz']
lista.append('Carol')

# Forma mais simples:

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])


# Esses dois for's faz a mesma coisa que o de cima:

# for item in enumerate(lista):
#     indice, nome = item 
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla: ')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')