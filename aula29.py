"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:  # Vai encontrar a exceção (erro) rapidamente e parar o bloco de código, ou seja, ele vai tentar executar o bloco se possível.
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:  # Vai ser executado caso o try encontre uma exceção.
    print('Isso não é um número')