# by mjos 2025-09-17
import numpy as np
def insert(a):
    if not np.all(np.sort(a) == range(1, len(a)+1)):
        raise RuntimeError('a is not a permutation of 1..len(a)')
    # end
    r=np.zeros(len(a)+1,2) # result
    h=0 # head
    #print(r)
    for x in a:
        # x = the number to insert
        if h==0 or x<=h:
            # replace head
            r[x,1]=h
            h=x
        else:
            j=h
            while j!=0:
                # swap order of children
                k=r[j,2]
                r[j,2]=r[j,1]
                r[j,1]=k
                if k==0 or x<=k:
                    # replace head of subtree
                    r[x,1]=k
                    r[j,1]=x
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
