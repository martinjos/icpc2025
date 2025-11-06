#!/usr/bin/env python3

import sys
import numpy as np
import timeit
from insert import insert
from removeBoth import removeBoth

def checkRemoveBoth(n=int(2e5)):
    rng = np.random.default_rng()
    p=rng.permutation(range(1,n+1))
    t=insert(p)
    r=removeBoth(t)
    t2=insert(r[0,:])
    t3=insert(r[1,:])
    if not np.all(t==t2):
        raise RuntimeError('First permutation is incorrect.')
    # end
    if not np.all(t==t3):
        raise RuntimeError('Last permutation is incorrect.')
    # end
    timer=timeit.Timer(lambda: removeBoth(t))
    nruns,tot=timer.autorange()
    return tot/nruns
# end

def main(n=int(2e5)):
    n = int(n)
    s=checkRemoveBoth(n)
    print(s)
# end

if __name__ == '__main__':
    main(*sys.argv[1:])
# end