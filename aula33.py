#AULA 33 
#EXERCICIOS - ENUNCIADOS
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = '10'

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Este número é divisivel por 2!')
    else: 
        print('Este numero não é divisivel por 2!')
else: 
    print('Este numero não é um inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = 10
hora_int = int(hora)

bom_dia = (hora_int>-1) and (hora_int<12)
boa_tarde = (hora_int>11) and (hora_int<18)
boa_noite = (hora_int>17) and (hora_int<24)

if bom_dia:
    print('Bom dia!')

elif boa_tarde:
    print('Boa tarde!')

elif boa_noite:
    print('Boa noite!')

else: 
    print('Horário inválido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = 'julia'

nome_letras = len(nome)

if nome_letras<=4:
    print('Seu nome é curto')
elif nome_letras==5 or nome_letras==6:
    print('Seu nome é normal')
elif nome_letras > 6:
    print('Seu nome é muito grande')