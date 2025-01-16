"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condicões no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 99  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1  # confere se a velocidade do carro passou o limite permitido
local_menor_range = local_carro >= (LOCAL_1 - RADAR_RANGE)  # calcula o range (ou distância do radar), subtraindo o valor 100 com o range que é 1 (= 99)
local_maior_range = local_carro <= (LOCAL_1 + RADAR_RANGE)  # calcula o range (ou distância do radar), somando o valor 100 com o range que é 1 (= 101)
carro_passou_radar_1 = local_menor_range and local_maior_range  # após realizar o calculo e estiver entre 99 a 101, significa que o carro passou pelo radar 
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1  # após a checagem de que se o carro passou o radar e a velocidade do carro estiver acima do permitido, então ele será multado

if vel_carro_pass_radar_1:  # verifica o limite do carro
    print('Velocidade ultrapassou o limite!')

if carro_passou_radar_1:  # verifica se passou o radar
    print('Carro passou RADAR 1')

if carro_multado_radar_1:  # verifica se as duas condições anteriores são verdadeiras e multa o carro
    print('Carro multado em RADAR 1')