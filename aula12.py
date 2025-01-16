# "..." ou também conhecido como "Ellipsis", é uma forma de marcador, ou seja, você consegue deixar um bloco de código "vazio" sem que o python considere aquilo um erro. (Você pode usar isso para escrever a lógica quando achar viável).

nome = 'Paulo Gobbi'
altura = 1.70
peso = 60
imc = peso // (altura * altura) # // para pegar a divisão inteira

print('O', nome, 'tem', str(altura) + ', pesa', peso, 'quilos e seu IMC é', imc)

# Paulo Gobbi tem 1.70 de altura, pesa 60 quilos e seu IMC é 20.
# Cálculo do IMC: peso/(altura x altura)