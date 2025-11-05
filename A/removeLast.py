# by mjos 2025-09-18
# remove the deepest left-chain node (repeatedly until empty).
# leave t intact; just return ordered list of removed nodes.
def removeLast(t):
    t=[t]
    h=1
    a=np.zeros(1,np.size(t,1))
    s=np.zeros(1,np.size(t,1))
    #print(t)
    counts=[]
    for i=np.size(t,1):-1:1:
        # find last candidate (left-chain node with no right child).
        # a candidate may only be traversed if its left child consists of only a single node.
        p=0; j=h
        sp=0
        count=1
        while j!=0 and (t(j,1)!=0 or t(j,2)!=0):
            if t(j,2)==0:
                # candidate
                count=count+1
                jj=t(j,1)
                if t(jj,1)!=0 or t(jj,2)!=0:
                    # left child has more than one node - traversal forbidden
                    break
                # end
            # end
            p=j
            sp=sp+1; s(sp)=p
            j=t(p,1)
        # end
        if j==0:
            raise RuntimeError('failed to complete - last left-chain node has a right child')
        # end
        #print(count)
        counts=[counts count]
        # remove the node
        if j==h:
            h=t(j,1)
        else:
            t(p,1)=t(j,1)
        # end
        t(j,1)=0 # just for display
        # swap all of the ancestors' children
        while sp>0:
            k=s(sp); sp=sp-1
            z=t(k,2)
            t(k,2)=t(k,1)
            t(k,1)=z
        # end
        # store identity of removed node
        a(i)=j
        #print(t)
    # end
    return a
# end
