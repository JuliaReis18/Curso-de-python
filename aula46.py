#AULA 46 - for + continue, break, else, etc

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue 

    if i == 8:
        print('i é 8, seu else não executará...')
        break

    for j in range(1,3):
        print(i, j) #i = linhas, j= colunas ( o ultimo n nunca conta)

else:
    print('For completo com sucesso!')