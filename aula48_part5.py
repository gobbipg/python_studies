"""
Cuidados com dados mutáveis
= - copiado o valor (imtáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Gobbi', 'Anne', 10, True, 1.9]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_a)