"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = iter('Paulo')  # __iter__()

print(next(texto))  # __next__()
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# print(next(texto))  # erro avisando que não tem mais o que mostrar.

####################

texto_2 = 'Gobbi'  # iterável
# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra= next(iteratador)
#         print(letra)

#     except StopIteration:
#         break

### O que while fez acontecer foi exatamente a mesma coisa que isso aqui: (por debaixo dos panos)

for letra in texto:
    print(letra)