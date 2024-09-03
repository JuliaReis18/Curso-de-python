#AULA 35 
#WHILE E BREAK (repeticoes)

#while - enquanto

condicao = True 

while condicao:
    nome = input('Qual o seu nome?')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')



#KEYBOARDINTERRUPT = CNTRL C