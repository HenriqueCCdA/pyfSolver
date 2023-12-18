project('pyfsolver',
  ['c', 'fortran'],
  version : '0.1.0',
  meson_version: '>= 1.3.0',
  default_options : [
    'warning_level=3',
    'buildtype=release',
  ]
)

py = import('python').find_installation(pure: false)

py.install_sources(
  'src/pyfsolver/__init__.py',
  'src/pyfsolver/__main__.py',
  'src/pyfsolver/blas.py',
  'src/pyfsolver/coo.py',
  'src/pyfsolver/cli.py',
  'src/pyfsolver/solver.py',
  'src/pyfsolver/py.typed',
  subdir: 'pyfsolver',
)

incdir_numpy = run_command(py,
  [
    '-c',
    'import os; import numpy; print(os.path.relpath(numpy.get_include()))'
  ],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
  [
    '-c',
    'import os; import numpy.f2py; print(os.path.relpath(numpy.f2py.get_include()))'
  ],
  check : true
).stdout().strip()

fortranobject_c = incdir_f2py / 'fortranobject.c'

lib_source = custom_target('_lfsolvermodule.c',
  input : ['src/library/api.f90'],
  output : ['_lfsolvermodule.c', '_lfsolver-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', '_lfsolver', '--lower']
)

inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module('_lfsolver',
    [
      'src/library/api.f90',
      'src/library/blas.f90',
      'src/library/pcg.f90',
      lib_source,
    ],
    fortranobject_c,
    include_directories: [inc_np],
    install: true,
    subdir: 'pyfsolver',
)
