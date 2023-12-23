import pytest

import numpy as np

from pyfsolver.coo import COO, Vector
from pyfsolver.numpy.solver import pcg


@pytest.mark.unity
@pytest.mark.math
def test_pcg():
    a = COO(
        data=np.array([1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0], dtype=np.float64),
        row=np.array([0, 0, 0, 1, 1, 2, 1, 2, 2], dtype=np.int32),
        col=np.array([0, 1, 2, 1, 2, 2, 0, 0, 1], dtype=np.int32),
        nnz=9,
    )
    b = Vector(
        data=np.array([2.0, 6.0, 1.0], dtype=np.float64),
        n=3,
    )
    x = Vector(
        data=np.zeros_like(b.data, dtype=np.float64),
        n=3,
    )

    pcg(a, b, x)

    assert x.data[0] == pytest.approx(1.6605166051660516)
    assert x.data[1] == pytest.approx(0.9446494464944649)
    assert x.data[2] == pytest.approx(0.5018450184501844)
