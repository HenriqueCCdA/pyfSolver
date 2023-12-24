# PyFortran

Projeto simples para explorar `interoperabilidade` entre o `Fortran` e o `Python`. Para essa tal foi utilização o `f2py`. O `f2py` gera automaticamente um wrapper em `C` para depois compilar uma lib `cpython`. Esse pacote faz parte no `numpy`. O `f2py` usa `meson` para configurar o `build` da `lib`. O `build-system` precisa do `numpy` e do  `meson-python`. Além disso o `meson` pode ser utilizando para fazer os testes de inidades na camada do `Fortran`.

Lista de ferramentas:

- [f2py](https://numpy.org/doc/stable/f2py/)
- [meson](https://mesonbuild.com/)
- [meson-python](https://mesonbuild.com/meson-python/)
- [build](https://pypa-build.readthedocs.io/en/latest/)

Todo o código `Fortran` está isolado em [library](src/library). Os testes da camada de `Fortran` estão na subpasta [fortan](tests/fortran/)

## Instalando

Criar a o ambiente virtual:

```bash
python -m venv .venv --upgrade-deps
```

Após de ativar o ambiente virtual basta fazer

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

Para executar usando a interface `fortran`:

```bash
pyfsolver fortran sist3.mtx sist3_b.mtx
```

Para executar usando apenasa o `numpy` :

```bash
pyfsolver numpy sist3.mtx sist3_b.mtx
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

Para qualidade temos configurado o `black`, `isort`, `flake8` e `mypy`. Para executar essa ferramentas a cada comite pode-se instalar o `precommit`:

```bash
pre-commit  install
```

ou manualmente rodar formatador, linter e os testes:

```bash
task fmt
task linter
task test
```

Além disso temo um `CI` configurado. 
