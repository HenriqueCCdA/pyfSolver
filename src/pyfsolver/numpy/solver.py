import numpy as np

from pyfsolver.coo import COO, Vector
from pyfsolver.numpy.blas import matvec_coo


def predcond_diagonal(a: COO, neq: int) -> np.ndarray:
    m = np.zeros(neq, dtype=np.float64)
    for i in range(a.nnz):
        if a.row[i] == a.col[i]:
            m[a.row[i]] = 1.0e0 / a.data[i]

    return m


def _pcg(a: COO, b: np.ndarray, x: np.ndarray, neq: int, tol: float, max_it: int, fprint: bool) -> np.ndarray:
    # precond
    m = predcond_diagonal(a, neq)

    # chute inicial
    x[:] = 0.0
    # conv = tol * |(M-1)b|m = tol(b,M(-1)b)/
    z = m * b
    d = float(np.dot(b.T, z))
    norm_b_m = np.sqrt(d)
    conv = tol * norm_b_m
    # .........................................................................

    # ... ||b||
    norm_b = np.sqrt(float(np.dot(b.T, b)))
    # .........................................................................

    # ...
    # ... r0 = b - Ax0
    r = b - matvec_coo(a, x)
    # ... z0 = (M-1)r0
    z = m * r
    # ... p0 = r0
    p = z.copy()
    # .........................................................................

    # ... ( r(0),z(0) ) = ( r(0), (M-1)r0 )
    d = float(np.dot(r.T, z))
    # .........................................................................

    # ...
    for j in range(1, max_it):
        # z = np.dot(a,p)
        matvec_coo(a, p, z)

        # alpha =( r(j),z(j) ) / ( Ap(j), p(j) ))
        alpha = d / float(np.dot(z.T, p))

        # x(j+1) = x(j) + alpha*p
        x += alpha * p
        # r(j+1) = r(j) - alpha*Ap
        r -= alpha * z
        # z  = (M-1)r0
        z = m * r

        # ( r(j+1),(M-1)r(j+1) ) = ( r(j+1),z )
        di = float(np.dot(r.T, z))
        # beta = ( r(j+1),(M-1)r(j+1) ) / ( r(j),r(j) )
        beta = di / d

        # p(j+1) = (M-1)r(j+1) + beta*p(j) = z + beta*p(j)
        p = z + beta * p

        d = di
        if np.sqrt(abs(d)) < conv:
            break

    #  Energy norm: xTAx
    matvec_coo(a, x, z)
    xkx = float(np.dot(x.T, z))
    # .........................................................................

    # || x ||
    norm_x = np.sqrt(float(np.dot(x.T, x)))

    stry = "(PCG) solver:\n"
    stry += "Solver tol           = {0:20.10E}\n"
    stry += "Number of equations  = {1:20}\n"
    stry += "Number of iterations = {2:20}\n"
    stry += "|| xKx ||            = {3:20.10E}\n"
    stry += "|| x ||              = {4:20.10E}\n"
    stry += "|| b ||              = {5:20.10E}\n"

    if fprint:
        print(stry.format(tol, j, neq, xkx, norm_x, norm_b))
    # .........................................................................

    return x


def pcg(a: COO, b: Vector, x: Vector, tol: float = 1e-14, maxit: int = 5_000, fprint: bool = False):
    _pcg(a, b.data, x.data, b.n, tol, maxit, fprint)
