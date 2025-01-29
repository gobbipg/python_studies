"""
Introdução as funções (def) em Python 
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def imprimir(a, b, c):  # os parâmetros seriam variáveis externas, então pode declarar mais de uma se quiser
    print(a, b, c)

imprimir(1, 2, 3)  
imprimir(4, 5, 6)  # os argumentos (ou valores) pode mudar de uma chamada da função pra outra
# na primeira chamada da função "imprimir" vai exibir 1, 2, 3. Já na segunda vai exibir 4, 5, 6, mas a função continua sendo a mesma (imprimir)


def saudacao(nome='Sem nome'):  # aqui dentro é chamado de "parâmetro"
    print(f'Olá, {nome}!')

saudacao('Luiz')  # aqui dentro é chamado de "argumento"
saudacao('Claudio')
saudacao('Paulo')
saudacao()  # vai exibir "Sem nome"
