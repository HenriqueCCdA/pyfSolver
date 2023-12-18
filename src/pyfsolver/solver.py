import numpy as np

from pyfsolver._lfsolver import pcg as _pcg
from pyfsolver.coo import COO


def pcg(a: COO, b: np.ndarray, x: np.ndarray, *, tol: float = 1e-11, maxit: int = 100, fprint: bool = False):
    _pcg(a.data, a.row, a.col, b, x, tol, maxit, fprint)
