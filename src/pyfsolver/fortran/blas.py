import numpy as np

from pyfsolver._lfsolver import matvec as _matvec
from pyfsolver.coo import COO


def matvec(a: COO, x: np.ndarray, y: np.ndarray) -> None:
    _matvec(a.data, a.row, a.col, x, y)
