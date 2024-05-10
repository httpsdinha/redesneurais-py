import numpy as np
import sigmoid


entradas = np.array([0.5,0.5,0.5])
pesos = np.array([-0.017, -0.893, 0.148])

def soma(e, p):
    return e.dot(p)
#dot product / produto escalar


s = soma(entradas, pesos)

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)
s = sigmoid.sigmoid(-0.424)
print('Step: ', r)
print('Sigmoid: ', s)