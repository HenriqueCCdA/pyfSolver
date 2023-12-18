# PyFortran

Projeto simples para explorar `interoperabilidade` entre o `Fortran` e o `Python`. Para essa comunicação foi utilização o `f2py`. O `f2py` gera automaticamente um wrapper em `C` para depois compilar uma lib `cpython`. Esse pacote faz parte no `numpy`. O `f2py` usa `meson` para configurar o `build` da `lib`. O `build-system` precisa do `numpy` e do  `meson-python`.

Lista de ferramentas:

- [f2py](https://numpy.org/doc/stable/f2py/)
- [meson](https://mesonbuild.com/)
- [meson-python](https://mesonbuild.com/meson-python/)
- [build](https://pypa-build.readthedocs.io/en/latest/)

## Instalando

Criar a o ambiente virtual:

```bash
python -m venv .venv --upgrade-deps
```

Apos de ativar o ambiente virtual basta fazer

```bash
source .venv/bin/activate
```

## Dev no modo editavel

Instalando as dependencias `dev` no modo `editavel`.

```bash
pip install meson-python meson ninja numpy
pip install --no-build-isolation --editable ".[dev]"
```

## Dev

Instalando as dependencias `dev`.

```bash
pip install ".[dev]"
```

## Executando

Para executar:

```bash
pyfsolver run sist3.mtx sist3_b.mtx
```

## Rodandos os teste

```bash
task test
```

## Gerando pacote

```bash
task package
```

## Commit

Para qualidade temos configurado `black`, `isort`, `flake8` e `mypy`. Para executar essa ferramentas pode-se instalar o precommit:

```bash
pre-commit  install
```

ou manumalmente rodar formatador, linter e os testes:

```bash
task fmt
task linter
task test
```
