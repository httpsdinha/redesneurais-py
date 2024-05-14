import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

def delta(e, d):
    return e * d


entradas = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])

saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                  [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017], [-0.893], [0.148]])

epocas = 100
momento = 1
taxaAprendizagem = 0.3

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1) 

    erroCamadaSaida = saidas - camadaSaida
    mediaAbs = np.mean(np.abs(erroCamadaSaida))

    derivadaAtivacao = sigmoidDerivada(camadaSaida)

    deltaSaida = erroCamadaSaida * derivadaAtivacao

    
    pesos1Transporta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transporta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

    camadaOcultaTransporta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransporta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    peso0 = (peso0 * momento) + (pesosNovo0 * taxaAprendizagem)
    
        
print(pesosNovo0)