"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# COMO EU FIZ (COM AUXILIO):

sequencia = []

print("Digite os primeiros 9 números do CPF (somente números): ")

for i in range(9):

    numero = int(input(f"Digite o {i+1}º número: "))
    sequencia.append(numero)

    regressiva = range(10, 1, -1)

    resultados = [num * reg for num, reg in zip(sequencia, regressiva)]

    soma_total = sum(resultados)

    soma_total_multi = soma_total * 10

    resto_divisao = soma_total_multi % 11

if resto_divisao > 9:
    resto_divisao = 0
    print(resto_divisao)

else:
    print(resto_divisao)


# SOLUÇÃO:

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:

    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)