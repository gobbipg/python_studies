"""
Exercício:
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados
    Exiba:
        Seu nome {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém ou não espaços
        Se nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
tem_espaco = ' '

if nome and idade:  # Certo
    print(f'Seu nome é {nome}') # Certo
    print(f'Seu nome invertido é {(nome[::-1])}') # Certo
    print(f'Seu nome contém ou não espaços: {(tem_espaco in nome)}') # Certo
    print(f'Seu nome tem {len(nome)} letras') # Certo 
    print(f'A primeira letra do seu nome é {(nome[0])}') # Certo
    print(f'A última letra do seu nome é {(nome[-1])}') # Certo

else:
    print('Desculpe, você deixou campos vazios.')

# OUTRA FORMA DE FAZER:

print(40 * '-')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:  # Certo
    print(f'Seu nome é {nome}') # Certo
    print(f'Seu nome invertido é {(nome[::-1])}') # Certo

    if ' ' in nome:  # Certo
        print('Seu nome CONTÉM espaços.')

    else:
        print('Seu nome NÃO contém espaços.')  

    print(f'Seu nome tem {len(nome)} letras') # Certo 
    print(f'A primeira letra do seu nome é {(nome[0])}') # Certo
    print(f'A última letra do seu nome é {(nome[-1])}') # Certo

else:
    print('Desculpe, você deixou campos vazios.')