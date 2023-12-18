import numpy as np

from pyfsolver.coo import COO
from pyfsolver.solver import pcg


def main():
    a = COO(
        data=np.array([1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0], dtype=np.float64),
        row=np.array([0, 0, 0, 1, 1, 2, 1, 2, 2], dtype=np.int32),
        col=np.array([0, 1, 2, 1, 2, 2, 0, 0, 1], dtype=np.int32),
        nnz=9,
    )
    b = np.array([2.0, 6.0, 1.0], dtype=np.float64)
    x = np.zeros_like(b, dtype=np.float64)

    print("Chamando PCG da lib fortran:\n")

    pcg(a, b, x, fprint=True)

    print(f"\nSolução do sistema: {x}")


if __name__ == "__main__":
    main()
