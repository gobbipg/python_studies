"""
Formação básica de strings 
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros 
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'

print(f'{variavel: >10}.') # O pad, é utilizado para preencher ou completar uma string ou número com caracteres adicionais até que ele atinja um comprimento.
print(f'{variavel: <10}.')
print(f'{variavel:$^11}.') # É possível completar os espaços com qualquer símbolo (teste antes!)
print(f'{1000.872346237846:0=+10,.2f}') # Formas de formatar um número
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!a}') # Utilizado para conversão de varáveis, mas muito pouco utilizado