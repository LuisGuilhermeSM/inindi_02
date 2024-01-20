import math
from numpy import cos, arange, pi
from pylab import show, legend, title, plot, figure


#help(arange)

T = 10
t = arange(0, 100, 0.1)
y = cos((2*pi*(1/T))*t) # O cosseno do numpy aceita arrays
# y = math.cos(t) da erro pois t é um array e esta função é apenas para variaveis unicas


"""
figure("Gráfico do cosseno") #Nome que aparecera na aba
#help(figure)
linesCosseno = plot(t, y, "g")
title("Teste do gráfico do cos")
legend(linesCosseno, "COS")
"""

l = t * 2 # Operação ocorre com em R

#show() #Para manter a aba na tela
a = "meu nome"
print(a[2])

a = 5+2j

def smallest_number(*args):
    print(args[1])
    print(len(args))

smallest_number(-10, -5, 5, 10)
#smallest_number(5, 10)

#help(map)

def funcion(x):
    x = x * 1.1
    return x

#print(map(func, 2))
print(list(map(funcion, [1, 2, 3])))
# A função map faz com que cada valor da lista seja aplicado na função funcion


g = lambda y: y*23

print(g(1/23))

class Carro(object):
    def __init__(self, estado):
        self.estado = estado

bmw = Carro('semi-novo')
print(bmw.estado) # 'semi-novo'