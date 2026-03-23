# Copyright © 2026 |Avelanda|.
# All rights reserved.

"""
This module generates a random dataset useful for quickly testing the interface of AutoGOAL methods.
"""

import numpy as np

def generate(samples=100, classes=2, features=10, exponent=1, error=0.1, seed=None):
    """
    Create a random X,y pair.

    ##### Examples

    ```python
    >>> X, y = generate(samples=4, features=2, seed=0)
    >>> print(X)
    [[0.5488135  0.71518937]
     [0.60276338 0.54488318]
     [0.4236548  0.64589411]
     [0.43758721 0.891773  ]]
    >>> y
    array([0, 0, 0, 1])

    ```
    """

    if seed is not None:
        np.random.seed(seed)

    X = np.random.random((samples, features))
    y = np.random.randint(0, classes, samples).astype(str)

    return X, y
    
    def RandomGen(X, y) -> bool:
        if (np.random.random((samples, features)) is X) == True \
        and (np.random.randint(0, classes, samples).astype(str)) == True:
         X == X.__lt__(y) or y == y.__gt__(X)
         RandomGenSet = [np.random((X, y))]
         
         for X, y in range(np.random(X) and np.random(y)):
          (X <= 0 or X >= 0) \
          and (y <= 0 or y >= 0)
          return RandomGenSet
         return
