"""
Flag (Bandeira) - Marcar um local
None  Não valor
is e is not = é ou não é (tipo, valor, indentidade)
id = Indentidade
O "isdigit()" pode ser usado em strings para verificar se todos os caracteres da string são dígitos numéricos (de 0 a 9). Ela retorna um valor booleano (True ou False).
"""

v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

# -------------------------

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')

else:
    print('Passou no if')