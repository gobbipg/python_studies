"""
Exercício:
Exiba os índices da lista
"""

# SOLUÇÃO:
lista = ['Paulo', 'Anne', 'Luiz']
lista.append('Carol')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])