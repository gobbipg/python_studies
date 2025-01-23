"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# O QUE EU TENTEI:

# lista = []

# while True:

#     opcoes = input(
#     '[i]nserir / [a]pagar / [l]istar\n'
#     'Digite umas das opções acima: '
#     )

#     if opcoes == 'i':
#         inserir = input('Digite o que deseja inserir: ')
#         lista.append(inserir)
#         print(list(enumerate(lista)))

#     elif opcoes == 'a':
#         ...

# SOLUÇÃO:
import os

lista = []

while True:

    print('Selecione uma opção.')
    opcao = input('[i]nserir / [a]pagar / [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('Por favor digite número inteiro.')

        except IndexError:
            print('Índice não existe na lista.')

        except Exception:
            print('Erro deseconhecido.')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar.')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
