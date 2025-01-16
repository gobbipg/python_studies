# if /    elif   / else
# se / se não se / se não

# if, elif e else, tem como função criar bolocos de códigos para o usuário interagir.
# Ou seja, o usuário tem que "suprir" uma necessidade do código para poder continuar executando o restante. 

# Primeiro vamos criar uma variável com input e perguntar para o usuário uma senha.
# Dependendo do que o usuário digitar, algum bloco será executado ou não. 

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Correto1')

elif condicao2:
    print('Correto2')

elif condicao3:
    print('Correto3')

elif condicao4:
    print('Correto4')

else:
    print('Errado.')

if 10 == 10:
    print('Verdadeiro')

print('Fora dos ifs.')