import pytest

import numpy as np

from pyfsolver.coo import COO
from pyfsolver.pyfortran.blas import matvec


def test_matvec():
    a = COO(
        data=np.array([1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0], dtype=np.float64, order="F"),
        row=np.array([0, 0, 0, 1, 1, 2, 1, 2, 2], dtype=np.int32, order="F"),
        col=np.array([0, 1, 2, 1, 2, 2, 0, 0, 1], dtype=np.int32, order="F"),
        nnz=9,
    )

    x = np.array([2.0, 2.0, 3.0], dtype=np.float64)
    y = np.zeros_like(x)

    matvec(a, x, y)

    assert y[0] == pytest.approx(3.3)
    assert y[1] == pytest.approx(12.4)
    assert y[2] == pytest.approx(3.6)
