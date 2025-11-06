#!/usr/bin/env python3

# by mjos 2025-09-19
# remove all left-chain nodes (repeatedly until empty).
# leave t intact; just return the number of permutations.
# findings: on randperm(64), takes several seconds and finds 2^21 permutations.
# number of permutations is always a power of 2 (even if input size is not).

import sys
import numpy as np
from insert import insert

def removeAll(t,v=False):
    ts=np.array([t])
    hs=np.array([1])
    chs=np.array([0])
    s=np.zeros((np.size(t,0)-1,), dtype=int)
    a=np.zeros((np.size(t,0)-1,), dtype=int)
    c=0
    q=0
    done=False
    while not done:
        if hs[q]==0:
            # tree is empty - so count permutation
            c=c+1
            if v:
                print(a)
            # end
        # end
        # find node to remove
        # will break unless backtracking
        while True:
            # lay foundation for next stage
            ts.resize((q+2,)+ts.shape[1:])
            ts[q+1,:,:]=ts[q,:,:]
            hs.resize((q+2,))
            hs[q+1]=hs[q]
            chs.resize((q+2,))
            chs[q+1]=0
            # find next left-chain node with no right child, or backtrack
            p=0; j=hs[q]
            sp=-1
            ch=0
            while j!=0:
                if ts[q,j,1]==0:
                    # no right child - so this is a candidate
                    ch=ch+1
                    if ch>chs[q]:
                        chs[q]=ch
                        break
                    # end
                # end
                # enter left child of node j
                p=j
                sp=sp+1; s[sp]=p
                j=ts[q,p,0]
            # end
            if j==0:
                # backtrack
                q=q-1
                if q==-1:
                    # failed to backtrack
                    break
                # end
            else:
                # found removable node
                break
            # end
        # end
        if q==-1:
            # done - no more paths to a solution
            break
        # end
        # remove the node
        if j==hs[q]:
            hs[q+1]=ts[q,j,0]
        else:
            ts[q+1,p,0]=ts[q,j,0]
        # end
        ts[q+1,j,0]=0 # just for display
        # swap all of the ancestors' children
        while sp>-1:
            k=s[sp]; sp=sp-1
            z=ts[q+1,k,1]
            ts[q+1,k,1]=ts[q+1,k,0]
            ts[q+1,k,0]=z
        # end
        # store identity of removed node
        a[len(a)-1-q]=j
        q=q+1
    # end
    return c
# end

def main(n=int(10)):
    n = int(n)
    rng = np.random.default_rng()
    a=rng.permutation(range(1,n+1))
    t=insert(a)
    c=removeAll(t,True)
    print(c)
# end

if __name__ == '__main__':
    main(*sys.argv[1:])
# end