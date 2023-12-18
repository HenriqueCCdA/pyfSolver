"""Funcionalidade de medição de tempo"""

from time import perf_counter as timer

from rich.console import Console

console = Console()


class Timer:
    def __init__(self, section_name: str = "Block", print_time: bool = True):
        self.section_name = section_name
        self.print_time = print_time
        self.start = 0.0
        self.end = 0.0
        self.time = 0.0

    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, *args):
        self.end = timer()
        self.time = self.end - self.start
        if self.print_time:
            console.print(
                f"{self.section_name} -> Time: {self.time:.2f} s",
                style="purple",
            )

    def get_wall_time(self) -> float:
        return self.time
