import numpy as np

from .solver import pcg


def main():
    a = np.array(
        [
            [1.0, 0.2, 0.3],
            [0.2, 6.0, 0.0],
            [0.3, 0.0, 1.0],
        ],
        order="F",
    )
    b = np.array([2.0, 6.0, 1.0], dtype=np.float64, order="F")
    x = np.zeros_like(b, dtype=np.float64, order="F")

    print("Chamando PCG da lib fortran:\n")

    pcg(a, b, x, fprint=True)

    print(f"\nSolução do sistema: {x}")


if __name__ == "__main__":
    main()
