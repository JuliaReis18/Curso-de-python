#AULA 44 - FOR/IN (while e utilizado para coisas variaveis)

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x)')
    repeticoes += 1

print(repeticoes)

texto = 'Python'
novo_texto = ''

for letra in texto: #para passar por cada letra da palavra 
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto)