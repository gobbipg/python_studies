"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '-', 'x + y + z =', x + y + z)

soma(1, 2, 3)  # aqui entra o posicionamento organizacional (onde x é 1 e y é 2)
soma(y=2, x=1, z=3)  # aqui entra o argumento nomeado (mesmo não estando na ordem que foi declarada nos parâmetros, o resultado é idêntico ao de cima, pois nomeamos os argumentos com o sinal de "=")
# soma(1, y=2, 3)  # vai gerar um erro, pois tudo que vem depois de um argumento nomeado também precisa ser nomeado (caso seja antes de um argumento nomeado, como o "1" ali, não tem erro, mas o "3" tem erro)
soma(1, y=2, z=3)  # assim não vai gerar nenhum erro, pois tudo que vem depois do primeiro nomeado (no caso o "y"), também está sendo nomeado
