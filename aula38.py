"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:

    coluna = 1

    while coluna <= qtd_linhas:     # while dentro de outro while, enquanto um for verdadeiro o outro irá ser executado até o fim da condição

        print(f'{linha=} {coluna=}')

        coluna += 1

    linha += 1


print('Acabou')