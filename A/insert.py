#!/usr/bin/python3

# by mjos 2025-09-17

import sys
import numpy as np

def insert(a):
    if not np.all(np.sort(a) == range(1, len(a)+1)):
        raise RuntimeError(f'a is not a permutation of 1..len(a): {a}')
    # end
    r=np.zeros((len(a)+1,2), dtype=np.int64) # result
    h=0 # head
    #print(r)
    for x in a:
        # x = the number to insert
        if h==0 or x<=h:
            # replace head
            r[x,0]=h
            h=x
        else:
            j=h
            while j!=0:
                # swap order of children
                k=r[j,1]
                r[j,1]=r[j,0]
                r[j,0]=k
                if k==0 or x<=k:
                    # replace head of subtree
                    r[x,0]=k
                    r[j,0]=x
                    # done inserting x
                    j=0
                else:
                    # enter left subtree
                    j=k
                # end
            # end
        # end
        #print(r)
    # end
    return r
# end

def main(*a):
    a = [int(x) for x in a]
    if len(a) == 1 and a[0] != 1:
        rng = np.random.default_rng()
        a = rng.permutation(range(1, a[0]+1))
    # end
    r = insert(a)
    print(r)
# end

if __name__ == '__main__':
    main(*sys.argv[1:])
# end