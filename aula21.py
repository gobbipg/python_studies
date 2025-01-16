# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas a condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 
# 0(zero), 0.0(zero ponto zero), ''(string vazia), False(falso).
# Também existe o tipo None que é usado para respresentar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '1234'

# if True:
# ...

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')


# Avaliação de curto circuito:

print(True and True and True)
print(True and False and True)
print(True and 0.0 and True)
print(True and None and True)
print(True and 0 and True)
print(bool(''))