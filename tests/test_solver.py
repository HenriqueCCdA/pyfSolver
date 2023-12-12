from pytest import approx
import numpy as np

from pyfsolver.solver import pcg


def test_pcg():

    a = np.array(
        [
            [1.0, 0.2, 0.3],
            [0.2, 6.0, 0.0],
            [0.3, 0.0, 1.0],
        ],
        order="F"
    )
    b = np.array([2.0, 6.0, 1.0], dtype=np.float64, order="F")
    x = np.zeros_like(b, dtype=np.float64, order="F")

    pcg(a, b, x)

    assert x[0] == approx(1.6605166051660516)
    assert x[1] == approx(0.9446494464944649)
    assert x[2] == approx(0.5018450184501844)
