# \r \n = CRLF utilizado para pular linhas
# \n = LF utlizado apenas em outros sistemas operacionais

print(12, 34, sep="-", end='##') # "sep" significa separador, ou seja, é possivel alterar o tipo de espaço que aparecerá
print(14, 38, sep='-', end="\n") # "end" é o que vai vir no final do argumento, no caso, aqui irá pular a linha somente
print(16, 1101)