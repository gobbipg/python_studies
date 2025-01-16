"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Paulo Gobbi'
outra_variavel = f'{string[:4]}ABC{string[5:]}'

print(string)
print(outra_variavel)
print(string.zfill(50))  # Métodos de string (visto na documentação do python, sempre bom buscar por lá para saber sobre ou como fazer algo específico. Ou apenas para estudar mais sobre a linguagem.)