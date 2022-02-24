#!/usr/bin/python3

import pkg_resources
from os.path import exists

# Информация о модулях которые должны быть установлены
modules_info = {
    'attrs': '21.4.0',
    'iniconfig': '1.1.1',
    'packaging': '21.3',
    'pluggy': '1.0.0',
    'py': '1.11.0',
    'pyparsing': '3.0.7',
    'pytest': '6.2.5',
    'toml': '0.10.2',
}

# Информация о bin файлах которые должны быть в системе
bin_files_info = ['pytest', 'py.test']

# Путь по которому модули должны быть установлены
modules_files_dir = '/usr/lib/python3.7/site-packages'

# Путь по которому bin файлы должны быть установлены
bin_files_dir = '/usr/bin'

def test_module_exists():
    print("\n")
    for module in modules_info:
        try:
            dist = pkg_resources.get_distribution(module)
            modname, modversion, modlocation = dist.key, dist.version, dist.location
            print(f"{module}: {modname} {modversion} {modlocation}")
            assert module == modname
            assert modules_info[module] == modversion
            assert modules_files_dir == modlocation
        except:
            print(f"{module} did not pass the test")
            assert False
    for f in bin_files_info:
        assert exists(f"{bin_files_dir}/{f}")