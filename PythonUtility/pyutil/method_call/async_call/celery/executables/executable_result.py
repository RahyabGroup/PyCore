from pyutil.method_call.async_call.celery.executables.executable_object import ExecutableObject

__author__ = 'Hooman Familrouhani'


class ExecutableResult(ExecutableObject):
    parent = None
    item = None
    is_iter = None

    def get_arg_value(self, previous_results):
        parent_result = self.parent.get_arg_value(previous_results)
        if self.is_iter:
            return parent_result[self.item]
        else:
            return getattr(parent_result, self.item)
