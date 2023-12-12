project('pyfsolver',
  ['c', 'fortran'],
  version : '0.1',
  meson_version: '>= 1.1.0',
  default_options : [
    'warning_level=3',
    'buildtype=release',
  ])

py = import('python').find_installation()

py.install_sources(
  'src/pyfsolver/__init__.py',
  'src/pyfsolver/__main__.py',
  'src/pyfsolver/solver.py',
  subdir: 'pyfsolver',
)

py_dep = py.dependency()

incdir_numpy = run_command(py,
  [
    '-c',
    'import os; import numpy; print(os.path.relpath(numpy.get_include()))'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
  ['-c', 'import os; import numpy.f2py; print(os.path.relpath(numpy.f2py.get_include()))'],
  check : true
).stdout().strip()

incdir_f2py = incdir_numpy / '..' / '..' / 'f2py' / 'src'
# inc_f2py = include_directories(incdir_f2py)
fortranobject_c = incdir_f2py / 'fortranobject.c'

lib_source = custom_target(
  input : ['src/lib/api.f90'],
  output : ['lpyfsolvermodule.c', 'lpyfsolver-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'lpyfsolver', '--lower']
)


inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module('lpyfsolver',
    [
      'src/lib/api.f90',
      'src/lib/blas.f90',
      'src/lib/pcg.f90',
      lib_source,
    ],
    fortranobject_c,
    include_directories: [inc_np],
    dependencies : [py_dep],
    install : true)
