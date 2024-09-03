#AULA 21
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

#cnrtl k cntrl c = comenta tudo / cntrl K cntrl U = descomenta

entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha')
senha_permitida = '123456'

print(entrada)
if entrada == "E" and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#AVALIAÇÃO DE CURTO CIRCUITO
print(True and False and True)
print(True and 0 and True)