import pytest

from pyfsolver.coo import read_matrix, read_vector


@pytest.mark.unity
def test_read_matrix():
    a = read_matrix("tests/coo_files/sist3.mtx")

    assert a.nnz == 9

    excepted = [1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0]

    for r, e in zip(a.data, excepted):
        assert r == pytest.approx(e)

    excepted = [0, 0, 0, 1, 1, 2, 1, 2, 2]

    for r, e in zip(a.row, excepted):
        assert r == e

    excepted = [0, 1, 2, 1, 2, 2, 0, 0, 1]

    for r, e in zip(a.col, excepted):
        assert r == e


@pytest.mark.unity
def test_read_vector():
    a = read_vector("tests/coo_files/sist3_b.mtx")

    assert a.n == 3

    excepted = [2.0, 6.0, 1.0]

    for r, e in zip(a.data, excepted):
        assert r == pytest.approx(e)
