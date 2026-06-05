import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("A lista deve conter nove números")

    matriz = np.array(lista).reshape(3, 3)

    calculations = {
        'mean': [
            matriz.mean(axis=0).tolist(),
            matriz.mean(axis=1).tolist(),
            matriz.mean().tolist()
        ],
        'variance': [
            matriz.var(axis=0).tolist(),
            matriz.var(axis=1).tolist(),
            matriz.var().tolist()
        ],
        'standard deviation': [
            matriz.std(axis=0).tolist(),
            matriz.std(axis=1).tolist(),
            matriz.std().tolist()
        ],
        'max': [
            matriz.max(axis=0).tolist(),
            matriz.max(axis=1).tolist(),
            matriz.max().tolist()
        ],
        'min': [
            matriz.min(axis=0).tolist(),
            matriz.min(axis=1).tolist(),
            matriz.min().tolist()
        ],
        'sum': [
            matriz.sum(axis=0).tolist(),
            matriz.sum(axis=1).tolist(),
            matriz.sum().tolist()
        ]
    }

    return calculations