#AULA 41 - EXERCICIO CALCULADORA COM WHILE 



while True:
    numero_1 = '5'
    numero_2 = '5'
    operador = '-'

    numeros_validos = None

    try:
        num_1_float =  float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os numeors digitados sao inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue 

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue 

    print('Dados validos! Confira o resultado de sua conta abaixo:')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)

    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    


    sair = 'sim'.lower().startswith('s')

    if sair is True:
        break
