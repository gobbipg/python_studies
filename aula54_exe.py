"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = []

while True:

    opcoes = input(
    '[i]nserir / [a]pagar / [l]istar\n'
    'Digite umas das opções acima: '
    )

    if opcoes == 'i':
        inserir = input('Digite o que deseja inserir: ')
        lista.append(inserir)
        print(list(enumerate(lista)))

    elif opcoes == 'a':
        ...

    