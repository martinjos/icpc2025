# by mjos 2025-09-18
# remove the deepest left-chain node (repeatedly until empty).
# leave t intact; just return ordered list of removed nodes.

import numpy as np

def removeLast(t):
    t=t.copy()
    h=1
    a=np.zeros((np.size(t,0)-1,), dtype=int)
    s=np.zeros((np.size(t,0)-1,), dtype=int)
    #print(t)
    counts=[]
    for i in range(np.size(t,0)-2, -1, -1):
        # find last candidate (left-chain node with no right child).
        # a candidate may only be traversed if its left child consists of only a single node.
        p=0; j=h
        sp=-1
        count=1
        while j!=0 and (t[j,0]!=0 or t[j,1]!=0):
            if t[j,1]==0:
                # candidate
                count=count+1
                jj=t[j,0]
                if t[jj,0]!=0 or t[jj,1]!=0:
                    # left child has more than one node - traversal forbidden
                    break
                # end
            # end
            p=j
            sp=sp+1; s[sp]=p
            j=t[p,0]
        # end
        if j==0:
            raise RuntimeError('failed to complete - last left-chain node has a right child')
        # end
        #print(count)
        counts.append(count)
        # remove the node
        if j==h:
            h=t[j,0]
        else:
            t[p,0]=t[j,0]
        # end
        t[j,0]=0 # just for display
        # swap all of the ancestors' children
        while sp>-1:
            k=s[sp]; sp=sp-1
            z=t[k,1]
            t[k,1]=t[k,0]
            t[k,0]=z
        # end
        # store identity of removed node
        a[i]=j
        #print(t)
    # end
    return a
# end
