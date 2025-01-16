# if /    elif   / else
# se / se não se / se não

# if, elif e else, tem como função criar bolocos de códigos para o usuário interagir.
# Ou seja, o usuário tem que "suprir" uma necessidade do código para poder continuar executando o restante. 

# Primeiro vamos criar uma variável com input e perguntar para o usuário uma senha.
# Dependendo do que o usuário digitar, algum bloco será executado ou não. 

senha = input('Digite a senha do sistema: ') # Variável com input

if senha == 'Cold':  # Se a "senha" for "Cold", execute esse próximo código...
    print('Acesso liberado!')  # Sempre se atente com a indentação nos if's, elif's e else's. A indentação é feita apenas apertando o TAB uma vez.

    print('Bem-Vindo!')

else:  # Caso o usuário digite outra coisa, execute esse código aqui...
    print('Acesso Negado!')

    print('Senha Incorreta.')

# Utilizando o if e else já podemos de certa forma limitar o que o usuário irá digitar.
# Com o elif, podemos ter mais de um bloco de comando dependendo do que o usuário digitar.

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'Entrar':  # Dependendo do que o usuário digitar, poderá aparecer um desses dois blocos, já o outro sera ignorado.
    print('Você entrou no sistema!')

    print('Bem-Vindo!')

elif entrada == 'Sair':  # Com o elif, podemos perguntar outra coisa para o usuário caso precisarmos de outra respota... Podemos utilizar o elif várias vezes.
    print('Você saiu do sistema!')

    print('Acesso Encerrado.')

else:
    print('Erro! Você não digitou corretamente.')