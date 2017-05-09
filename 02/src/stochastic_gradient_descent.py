import numpy as np
from numpy import pi
from sklearn.metrics import mean_squared_error as mse

def fit(X, Y, alpha=0.005, epsilon=0.005, max_iter=10000, h='linear'):
    errors = []
    theta = np.random.normal(-0.1, 1, np.shape(X)[1])
    
    h_functions = {'linear':lambda x: np.dot(theta, x), 
                   'logistic':lambda x: 1/(1 + np.exp( -1*np.dot(theta, x)))
                   }
    h = h_functions[h]

    cur_iter = 0
    e = mse(map(h, X), Y)
    while e > epsilon:
        errors.append(e)
        for x, y in zip(X, Y):
            theta += alpha*(y - h(x))*x
        if cur_iter == max_iter: return theta, errors
        e = mse(map(h, X), Y)
        cur_iter+=1
    return theta, errors
