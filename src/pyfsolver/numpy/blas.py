import numpy as np

from pyfsolver.coo import COO


def matvec_coo(a: COO, x: np.ndarray, y: np.ndarray | None = None) -> np.ndarray:
    if y is None:
        y = np.zeros_like(x)
    else:
        y[:] = 0.0e0

    for i in range(a.nnz):
        irow, icol = a.row[i], a.col[i]
        y[irow] += a.data[i] * x[icol]

    return y
