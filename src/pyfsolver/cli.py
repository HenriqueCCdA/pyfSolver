from pathlib import Path
from typing import Annotated

import numpy as np
import typer
from click import Context
from rich.console import Console

from pyfsolver.coo import Vector, read_matrix, read_vector
from pyfsolver.solver import pcg

console = Console()


def version_callback(value: bool):
    if value:
        str_ = "pyfsolver 0.1.0"
        console.print(str_)
        raise typer.Exit()


app = typer.Typer(add_completion=False, pretty_exceptions_show_locals=False)


@app.callback(invoke_without_command=True)
def typer_callback(
    ctx: Context,
    version: Annotated[
        bool, typer.Option("--version", "-v", help="Versão do FORM.", callback=version_callback)
    ] = False,
):
    if ctx.invoked_subcommand:
        return
    console.print("[yellow]Usage[/yellow]: [green]pyfsolver[/green] [OPTIONS] COMMAND [ARGS]...\n")
    console.print("[blue]--help[/blue] for more informations.")


@app.command()
def run(
    input_matrix: Annotated[Path, typer.Argument(..., help="Camanho do arquivo da matriz no formato .mtx.")],
    input_b: Annotated[Path, typer.Argument(..., help="Camanho do arquivo do vetor b no formato .mtx.")],
):
    """Resolvendo o sistema de equações."""
    a = read_matrix(input_matrix)
    b = read_vector(input_b)

    x = Vector(data=np.zeros_like(b.data), n=b.n)
    pcg(a, b, x, fprint=True)
