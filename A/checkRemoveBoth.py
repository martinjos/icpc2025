def checkRemoveBoth():
    p=randperm(2e5)
    t=insert(p)
    r=removeBoth(t)
    t2=insert(r[0,:])
    t3=insert(r[1,:])
    if not np.all(t[:]==t2[:]):
        raise RuntimeError('First permutation is incorrect.')
    # end
    if not np.all(t[:]==t3[:]):
        raise RuntimeError('Last permutation is incorrect.')
    # end
    s=timeit(@()removeBoth(t))
    return s
# end
