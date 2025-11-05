% by mjos 2025-09-19
% remove all left-chain nodes (repeatedly until empty).
% leave t intact; just return the number of permutations.
% findings: on randperm(64), takes several seconds and finds 2^21 permutations.
% number of permutations is always a power of 2 (even if input size is not).
function c=removeAll(t,v)
    ts=[t];
    hs=[1];
    chs=[0];
    s=zeros(1,size(t,1));
    a=zeros(1,size(t,1));
    c=0;
    q=1;
    done=0;
    while ~done
        if hs(q)==0
            % tree is empty - so count permutation
            c=c+1;
            if bitand(v,1)
                disp(a);
            end
        end
        % find node to remove
        % will break unless backtracking
        while 1
            % lay foundation for next stage
            ts(:,:,q+1)=ts(:,:,q);
            hs(q+1)=hs(q);
            chs(q+1)=0;
            % find next left-chain node with no right child, or backtrack
            p=0; j=hs(q);
            sp=0;
            ch=0;
            while j~=0
                if ts(j,2,q)==0
                    % no right child - so this is a candidate
                    ch=ch+1;
                    if ch>chs(q)
                        chs(q)=ch;
                        break;
                    end
                end
                % enter left child of node j
                p=j;
                sp=sp+1; s(sp)=p;
                j=ts(p,1,q);
            end
            if j==0
                % backtrack
                q=q-1;
                if q==0
                    % failed to backtrack
                    break;
                end
            else
                % found removable node
                break;
            end
        end
        if q==0
            % done - no more paths to a solution
            break;
        end
        % remove the node
        if j==hs(q)
            hs(q+1)=ts(j,1,q);
        else
            ts(p,1,q+1)=ts(j,1,q);
        end
        ts(j,1,q+1)=0; % just for display
        % swap all of the ancestors' children
        while sp>0
            k=s(sp); sp=sp-1;
            z=ts(k,2,q+1);
            ts(k,2,q+1)=ts(k,1,q+1);
            ts(k,1,q+1)=z;
        end
        % store identity of removed node
        a(length(a)+1-q)=j;
        q=q+1;
    end
end
