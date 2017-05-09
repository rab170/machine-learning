import numpy as np
from numpy import pi

def sgd(X, Y, alpha=0.005, epsilon=2, max_iter=10000):
    errors = []
    theta = np.random.normal(-0.1, 0.1, np.shape(X)[1])
    model = lambda x: np.dot(theta, x)
    cur_iter = 0
    e = np.sum((map(model, X) - Y)**2)
    while e > epsilon:
        errors.append(e)
        for x, y in zip(X, Y):
            theta += alpha*(y - np.dot(theta, x))*x
        if cur_iter == max_iter: return theta, errors
        e = np.sum((map(model, X) - Y)**2)
        cur_iter+=1
    return theta, errors
