import numpy as np
from removeLast import removeLast
from removeFirst import removeFirst

def removeBoth(t):
    r=np.array([removeLast(t), removeFirst(t)])
    return r
# end
