__author__ = 'root'


import inspect
import pkgutil


def import_all_subclasses_of(module_to_scan, base_class, scope=locals()):
    """
    :param module_to_scan: Module to scan.
    :param base_class: A base class to check.
    :param scope: globals(), locals() or a dict-like object.
    """
    path = module_to_scan.__path__
    for mod in pkgutil.iter_modules(path):
        module = mod[0].find_module(mod[1]).load_module(mod[1])

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, base_class) and name != base_class.__name__:
                scope[name] = obj
