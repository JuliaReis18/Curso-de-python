#AULA 23
entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha') or 'Sem senha'
print(senha_digitada)
senha_permitida = '123456'

print(entrada)
if entrada == "E" or "e" and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
