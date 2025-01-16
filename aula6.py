# conversão de tipos, coerção
# type convertion, typecasting, coercion é o ato de converter um tipo em outros tipos imutáveis e primitivos:
# str, int, float, bool

print(int('1'), type(int('1'))) # Convertendo um dado para número inteiro
print(type(float('1') + 1)) 
print(float('1') + 1, type(float('1') + 1)) # Convertendo um dado para número com casa decimal (ponto flutuante)
print(bool(' ')) # Caso não tenha nenhum valor descrito, o bool irá retornar False. Agora, caso tenha algum dado, nem que seja espaço, ele irá retornar True
print(bool('sim' == 'sim')) # Convertendo um dado para dado booleano (verdadeiro ou falso)
print(str(10) + 'b') # Convertendo um dado para string (texto)