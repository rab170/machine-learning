import numpy as np

class AdaBoost:
    
    def __init__(self, weak_classifier, n=10):
        self.classifiers = [lassifier for _ in xrange(n)]
        self.alpha = np.zeros(n)
        self.D = np.full([n, 0], 1.0/n)

    def fit(self, X, y):
        for classifier in self.classifiers:
            
            

            
