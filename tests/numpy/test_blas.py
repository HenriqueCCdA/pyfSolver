import pytest

import numpy as np

from pyfsolver.coo import COO
from pyfsolver.numpy.blas import matvec_coo


@pytest.fixture
def a():
    return COO(
        data=np.array([1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0], dtype=np.float64, order="F"),
        row=np.array([0, 0, 0, 1, 1, 2, 1, 2, 2], dtype=np.int32, order="F"),
        col=np.array([0, 1, 2, 1, 2, 2, 0, 0, 1], dtype=np.int32, order="F"),
        nnz=9,
    )


@pytest.fixture
def x():
    return np.array([2.0, 2.0, 3.0], dtype=np.float64)


@pytest.mark.unity
@pytest.mark.math
def test_matvec_pass_y(a, x):
    y = np.zeros_like(x)

    matvec_coo(a, x, y)

    assert y[0] == pytest.approx(3.3)
    assert y[1] == pytest.approx(12.4)
    assert y[2] == pytest.approx(3.6)


@pytest.mark.unity
@pytest.mark.math
def test_matvec_return_y(a, x):
    y = matvec_coo(a, x)

    assert y[0] == pytest.approx(3.3)
    assert y[1] == pytest.approx(12.4)
    assert y[2] == pytest.approx(3.6)


@pytest.mark.unity
@pytest.mark.math
def test_matvec_return_y_and_pass_need_by_the_same(a, x):
    y_old = np.zeros_like(x)

    y_new = matvec_coo(a, x, y_old)

    assert id(y_new) == id(y_old)

    assert y_new[0] == pytest.approx(3.3)
    assert y_new[1] == pytest.approx(12.4)
    assert y_new[2] == pytest.approx(3.6)
