# by mjos 2025-09-18
# remove the least deep left-chain node (repeatedly until empty).
# leave t intact; just return ordered list of removed nodes.
function a=removeFirst(t):
    t=[t]
    h=1
    a=zeros(1,size(t,1))
    s=zeros(1,size(t,1))
    #disp(t)
    for i=size(t,1):-1:1:
        # find first left-chain node with no right child
        p=0; j=h
        sp=0
        while j~=0 && t(j,2)~=0:
            p=j
            sp=sp+1; s(sp)=p
            j=t(p,1)
        # end
        if j==0:
            error('failed to complete - every left-chain node has a right child')
        # end
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
        #disp(t)
    # end
# end
