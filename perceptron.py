entradas = [1, 1]
pesos = [0.5, 0.5]

def soma(e, p):
    s = 0
    for i in range(2):
        s += e*p
    return s


s = soma(entradas, pesos)

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)
print(r)