from pyutil.method_call.async_call.celery.executables.executable_result import ExecutableResult

from pyutil.method_call.async_call.celery.dynamics.dynamic_object import DynamicObject

__author__ = 'Hooman Familrouhani'


class DynamicResult(DynamicObject):
    parent = None
    item = None
    is_iter = None

    def __init__(self, item, parent, is_iter=False):
        self.item = item
        self.parent = parent
        self.is_iter = is_iter

    def executable_instance(self):
        executable_result = ExecutableResult()
        executable_result.parent = self.parent.executable_instance()
        executable_result.item = self.item
        executable_result.is_iter = self.is_iter
        return executable_result

    def get_result(self):
        parent_result = self.parent.get_result()
        if self.is_iter:
            return parent_result[self.item]
        else:
            return getattr(parent_result, self.item)
