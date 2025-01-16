# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy 
# 0(zero), 0.0(zero ponto zero), ''(string vazia), False(falso).
# Também existe o tipo None que é usado para respresentar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '1234'

# if True:
# ...

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')


# Avaliação de curto circuito:

# print(0 or False or 0.0 or 'abc' or True)

# senha = 0 or False or 0.0 or 'abc' or True
# print(senha)

senha = input('Senha: ') or 'Sem senha.'
print(senha)