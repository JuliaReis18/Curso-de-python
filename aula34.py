#AULA 34 
#tipos built-in ,  documentação, imutáveis, métodos de string

string = 'julia'
outra_variavel = f'{string[:3]}ABC{string[3:]}'
print(outra_variavel)
print(string.capitalize())
print(string.upper())
print(string.islower())
print(string.zfill(10)) #para preencher com 0's