# Outro tipo de formatação de strings:

a = 'AAAA'

b = 'BBBB'

c = 1.1

string = 'b= {nome2} a= {nome1} a= {nome1} c= {nome3:.2f}'
formato = string.format(
    
    nome1= a, nome2= b, nome3= c
) 
# Apenas quebrei a linha para poder visualizar melhor os dados e parâmetros.

print(formato)