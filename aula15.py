# A função "input" é utilizada para perguntar algo ao usuário, no entanto ela não guarda a resposta.
# O único jeito de guardar a resposta seria colocando o input em uma variável, como nos exemplos abaixo.

nome = input('Qual o seu nome: ') # Input sempre será uma string.

print(f'Seu nome é {nome}.')

num_1 = input('Digite um número: ')
num_2 = input('Digite mais um número: ')

int_num_1 = int(num_1) # Utilizar outra variável para verificar se o usuário digitou realmente um número pode ser útil futuramente...
int_num_2 = int(num_2)

print(f'A soma dos dois números é: {int_num_1 + int_num_2}')