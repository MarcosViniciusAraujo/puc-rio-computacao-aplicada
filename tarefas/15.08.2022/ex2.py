'''
Author: @Marcos_Vinicius_Araujo

created_at: 11/08/2022
'''

from math import sqrt


def areaRetangulo(l1, l2):
    return l1*l2

def hipotenusa(c1, c2):
    return sqrt(c1**2 + c2**2)

def areaTotal(a, b, c, d, e):
    ret1 = areaRetangulo(a, b)
    ret2 = areaRetangulo(c, d)
    tri = areaRetangulo(d, a) / 2
    ret3 = areaRetangulo(e, hipotenusa(d, a))

    print("Ret1: {} - Ret2: {} - Ret3: {} - Tri: {}".format(
        ret1,
        ret2,
        ret3,
        tri
    ))

    return ret1 + ret2 + ret3 + tri


    
result = input('Digite o valor dos lados, separados por ",": ').split(',')

a = int(result[0])
b = int(result[1])
c = int(result[2])
d = int(result[3])
e = int(result[4])

print(f"Area total: {areaTotal(a,b,c,d,e)}")


def concat_diferente(word):
    pref = word[:2]
    suff = word[-2:]

    return word + "".join([pref+suff for i in range(4)])

print(concat_diferente('abcdefg'))