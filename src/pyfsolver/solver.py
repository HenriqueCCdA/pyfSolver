import numpy as np
from lpyfsolver import pcg as _pcg


def pcg(a: np.ndarray, b: np.ndarray, x: np.ndarray, *, tol: float = 1e-11, maxit: int = 100, fprint: bool = False):
    _pcg(a, b, x, tol, maxit, fprint)
