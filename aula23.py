# Operadores lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Não digitou nada')

else:
    print('Ok')

print(not True) # False
print(not False) # True