#AULA 28
nome = input('Digite o seu nome abaixo:')
if nome:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
    print(f'Seu nome contém {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe, vc deixou campos vazios')