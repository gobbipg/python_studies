"""
Fatiamento de strings 
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'

print(variavel[-7]) # Fatiamento
print(variavel[4:8]) # Possível omitir o inicio ou o fim
print(variavel[-5:-1]) # Fatiamento com número negativo
print(len(variavel)) # Faz a contagem de caracteres, caso coloque [] com algum número depois da variável, ele irá retornar o único caractere da string. 
print(variavel[::-1]) # Inverteu a string
print(variavel[-4::-1]) 