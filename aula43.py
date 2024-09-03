#AULA 43 - LETRANDO STRINGS COM PYTHON


frase = 'aaaooouu'.lower()


# print(frase.count('python'))

i = 0 
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_apareceu = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_apareceu:
        apareceu_mais_vezes = quantas_vezes_apareceu
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1


print(f'A letra que apareceu mais vezes foi a {letra_que_apareceu_mais_vezes}, que apareceu {apareceu_mais_vezes} vezes.')