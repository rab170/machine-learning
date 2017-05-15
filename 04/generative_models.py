
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal

class GaussianDiscriminant(object):

    def __init__(self, df):
        features = [col for col in list(df) if col != 'label']
        ones = (df.label == 1)        
        zeros = (df.label == 0)
        m = df.shape[0]
        
        phi = (1.0/m) * ones.sum()
        mu_0 = df[zeros][features].mean()
        mu_1 = df[ones][features].mean()

        n = len(features)
        cov = np.zeros(shape=(n, n))        
        deltas = df[zeros][features] - mu_0
        deltas = deltas.append(df[ones][features] - mu_1, ignore_index=True)
        for i in range(m):
            delta = np.array(deltas.iloc[i])
            delta_t = np.transpose(delta)
            cov[:, :] += np.array([a_i*delta for a_i in delta])
        cov = (1.0/m)*cov

        self.n = n
        self.phi = phi
        self.cov = cov
        self.mu_0 = mu_0.as_matrix()
        self.mu_1 = mu_1.as_matrix()
        self.p_0 = lambda x: multivariate_normal.pdf(x, self.mu_0, self.cov)
        self.p_1 = lambda x: multivariate_normal.pdf(x, self.mu_1, self.cov)
        self.features = features

    def pdfs(self, x):
        x = pd.to_numeric(x[self.features], errors='raise').as_matrix()
        return [self.p_0(x), self.p_1(x)]
