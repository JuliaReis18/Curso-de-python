#AULA 14 

#formatação de strings com método format

a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b , c) #com o metodo format, as variaveis inseridas nas chaves serão na mesma ordem que quando colocadas nos parenteses

#OU

string2 = 'a={nome3} b={nome2} c={nome3}'
formato2 = string2.format(nome1=a,nome2=b,nome3=c)


print(formato)
print(formato2)

#erro de range = buscar algo que ja acabou 