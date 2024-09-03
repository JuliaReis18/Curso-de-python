#AULA 25
#operadores in e not in
#strings são interáveis

nome = "Julia"
print(nome[2])
print(nome[4])
print('J' in nome)
print('J' not in nome)

nome = input('Digite o seu nome:')
encontrar = input('Digite que deseja encontar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}.')

#AULA 25
#interpolaçao básica de strings
#s - string
# f - float
# d e i - int
# x e X - hexadecimal

nome = 'Julia'
preco = 100.00
variavel = '%s, o preço total foi R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' %(1500,1500))