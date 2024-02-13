"""Aggregate module to give access to python tools for jokes """

from contextlib import suppress

ignore_if_module_not_found = suppress(ModuleNotFoundError, ImportError)

with ignore_if_module_not_found:
    import laugh  # pip install laugh to get this
    from laugh import *

with ignore_if_module_not_found:
    import pyjokes  # pip install pyjokes to get this
    from pyjokes import *

