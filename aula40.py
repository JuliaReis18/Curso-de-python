#AULA 40 - EXERCICIO GUIADO
#.......012345...
nome = 'Julia'
tam_nome = len(nome)

indice = 0
novo_nome = ''
while indice < tam_nome:
    letra = nome[indice]
    novo_nome+= f'{letra}*'
    indice += 1 

print(novo_nome)