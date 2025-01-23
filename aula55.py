"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')  # Ao importar o decimal, precisa aterar o número para uma string para que ele possa "arrendondar" o número.
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))  # round arredonda da mesma forma que o decimal ou :.2f, basta sinalizar a quantidade de casas decimais após a vírgula.