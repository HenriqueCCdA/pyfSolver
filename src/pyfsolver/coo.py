from dataclasses import dataclass
from pathlib import Path

from numpy import ndarray
from scipy import io


@dataclass(frozen=True)
class COO:
    data: ndarray
    row: ndarray
    col: ndarray
    nnz: int


@dataclass(frozen=True)
class Vector:
    data: ndarray
    n: int


# TODO: Verificar se a matriz e quadrada
def read_matrix(file: Path):
    """Le uma matriz no formato COO

    Args:
        file (Path): caminho do arquivo da matriz

    Returns:
        COO: retorna a matriz lida
    """
    a = io.mmread(file)

    return COO(a.data, a.row, a.col, a.nnz)


# TODO: Verificar se a matriz e quadrada
def read_vector(file: Path):
    """Le uma vetor no formato COO

    Args:
        file (Path): caminho do arquivo do vetor

    Returns:
        Vector: retorna o vetor lido
    """
    a = io.mmread(file)

    return Vector(a.copy(), a.shape[0])
