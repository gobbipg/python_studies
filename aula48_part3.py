"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#       0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Gobbi')  # Adicionei a string Gobbi ao final da minha lista numerica
nome = lista.pop()  # Aqui exclui o ultimo indice da minha lista (que era a string gobbi) / posso escolher qqlr indice para excluir, basta declarar no () no pop
print(lista, nome)
del lista[-1]  # Aqui eu deletei um indice da lista (caso não saiba qual o ultimo indice da lista, basta colocar o -1)
# lista.clear()  # Aqui eu limpei toda a lista
print(lista, nome)
lista.insert(2, '100')  # Aqui eu inseri novos dados e movi os indices, basta colocar dois argumentos nos (), o primeiro é o indice que vc irá mexer e depois é o dado novo que vc irá acrescentar
print(lista)