# "..." ou também conhecido como "Ellipsis", é uma forma de marcador, ou seja, você consegue deixar um bloco de código "vazio" sem que o python considere aquilo um erro. (Você pode usar isso para escrever a lógica quando achar viável).

nome = 'Paulo Gobbi'
altura = 1.70
peso = 60
imc = peso // (altura * altura) # // para pegar a divisão inteira

print('O', nome, 'tem', str(altura) + ', pesa', peso, 'quilos e seu IMC é', imc)

# Paulo Gobbi tem 1.70 de altura, pesa 60 quilos e seu IMC é 20.
# Cálculo do IMC: peso/(altura x altura)


# F-Strings:
# É possível formatar strings de algumas maneiras, uma delas é utilizando o "f" antes de iniciar a string.
# Ao colocar o f, você poderá escrever normalmente, apenas colocando chaves ( {} ) nas variáveis para que ela chame na string. Como no exemplo abaixo (linha_1).

linha_1 = f'{nome} tem {altura:.2f} de altura e pesa {peso:.1f} quilos e seu IMC é {imc:.2f}'

print(linha_1)