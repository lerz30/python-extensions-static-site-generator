import importlib
import sys
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    for path in directory:
        path.rglob('.py')
        load_module(path.as_posix(), path.stem)

def load_bundled():
    directory = Path(__file__).parent
    load_directory(directory)