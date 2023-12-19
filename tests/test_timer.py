from time import sleep

import pytest

from pyfsolver.timer import Timer


def test_exec_time():
    with Timer("Sec A", print_time=False) as time:
        sleep(1.0)

    assert time.get_wall_time() == pytest.approx(1.0, rel=1e-2)
