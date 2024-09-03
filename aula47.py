#AULA 47 - exercicio

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'melancia'

tentativas = input('Digite a letra:').lower()

repeticoes = 0

while tentativas not in palavra_secreta:
    repeticoes += 1
    tentativas = input(f'Tente novamente ({repeticoes})x')
    

print(repeticoes)


if tentativas in palavra_secreta:
    print(f'Parabéns! A letra {tentativas} está na palavra secreta.')
    print(f'Tentativas:{repeticoes}')
else:
    print('*')