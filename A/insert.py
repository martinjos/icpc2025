# by mjos 2025-09-17
function r=insert(a):
    if ~all(sort(a) == 1:length(a)):
        error('a is not a permutation of 1:length(a)')
    # end
    r=zeros(length(a),2) # result
    h=0 # head
    #disp(r)
    for i=1:length(a):
        x=a(i) # number to insert
        if h==0 || x<=h:
            # replace head
            r(x,1)=h
            h=x
        else:
            j=h
            while j~=0:
                # swap order of children
                k=r(j,2)
                r(j,2)=r(j,1)
                r(j,1)=k
                if k==0 || x<=k:
                    # replace head of subtree
                    r(x,1)=k
                    r(j,1)=x
                    # done inserting x
                    j=0
                else:
                    # enter left subtree
                    j=k
                # end
            # end
        # end
        #disp(r)
    # end
# end
