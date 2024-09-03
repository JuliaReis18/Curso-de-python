#AULA 30
#CONSTANTE = variaveis que nao vao mudar

velocidade = 61
local_carro_1 = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_passou_radar = velocidade > RADAR_1
carro_passou_radar1 = local_carro_1 >= (LOCAL_1 - RADAR_RANGE) \
    and local_carro_1 <= (LOCAL_1 + RADAR_RANGE)

if velocidade_passou_radar:
    print('O carro passou da velocidade')

if carro_passou_radar1:
    print('O carro passou no radar 1!')

if carro_passou_radar1 and velocidade_passou_radar:
    print('O CARRO FOI MULTADO EM RADAR 1')

    #DICAS = CURSOR NA VARIAVEL E F2 ALTERA A VARIAVEL EM TODOS OS LOCAIS QUE ELA E UTILIZADA