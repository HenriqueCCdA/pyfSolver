from pyfsolver._lfsolver import pcg as _pcg
from pyfsolver.coo import COO, Vector


def pcg(a: COO, b: Vector, x: Vector, *, tol: float = 1e-14, maxit: int = 5000, fprint: bool = False):
    _pcg(a.data, a.row, a.col, b.data, x.data, tol, maxit, fprint)
