import sys
import numpy as np
from cython cimport view
from libc.stdint cimport int64_t
from A.insert import insert

cdef public void A_insert(int64_t *a, int64_t n, int64_t *b):
    cdef view.array a_view = <int64_t[:n]> a
    cdef view.array b_view = <int64_t[:n,:2]> b
    t = insert(np.array(a_view))
    assert (t.dtype == np.int64
            and t.shape == (n+1, 2))
    cdef int64_t[:,:] t_view = t[1:,:]
    b_view[:,:] = t_view[:,:]
# end