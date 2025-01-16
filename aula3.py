"""
Python = Linguegem de Programação
Tipo de Tipagem = Dinâmica / Forte 
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

print(1234)

# Aspas simples 
print('Paulo Gobbi')
print(1, 'Paulo "Gobbi"') #

# Aspas duplas
print('Paulo Gobbi')
print(2, "Paulo 'Gobbi'") #

# Escape
print("Paulo \"Gobbi\"") # ao utilizar barra invertida e aspas logo depois, fará com que o interpretador "pule" aquelas aspas e siga para o resto da string, mas as aspas aparecerão.

# r
print(r"Paulo \"Gobbi\"") # aqui o "r" é basicamente a mesma coisa do escape, no entanto, ele vai mostrar tudo o que estiver na string

# o "escape e o "r" dificilmente você irá utilizar eles em algum código, pois existe um jeito mais simples de exibir aspas em suas strings, como está nos exemplos acima marcados com "#" na frente