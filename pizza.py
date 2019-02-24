from math import *
from functools import reduce


def factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    a = 1
    return [a] + factors

def pairFactors(n):
    factors = factorization(n)
    tmp = factors[:]
    dic = {}
    if len(factors) == 1:
        return {}
    elif len(factors) == 2:
        return {(factors[0],factors[1]):factors[0]*factors[1],(factors[1],factors[0]):factors[0]*factors[1]}
    else:
        for idx,valu in enumerate(factors):
            val =factors[idx]
            tmp.pop(idx)
            mul = reduce(lambda x, y: x*y, tmp)
            dic[(val,mul)] = mul*val
            dic[(mul,val)] = mul*val
            tmp = factors[:]
    #retdic = sorted(dic)
    return dic
def shapesOfN2(x,y):
    ret = {}
    for i in reversed(range(x,y+1)):
        tmp =  pairFactors(i)
        ret = {**ret, **tmp}
    return ret

def main():
    tmp = shapesOfN2(1,12)
    print(tmp)

if __name__ == "__main__":
    main()