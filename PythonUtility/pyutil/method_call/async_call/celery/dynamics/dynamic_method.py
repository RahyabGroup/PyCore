import uuid

from pyutil.method_call.async_call.celery.context import Context

from pyutil.method_call.async_call.celery.executables.executable_method import ExecutableMethod
from pyutil.method_call.async_call.celery.dynamics.dynamic_object import DynamicObject

__author__ = 'Hooman Familrouhani'


class DynamicMethod(DynamicObject):
    dynamic_method_id = None
    dynamic_method_method = None
    dynamic_method_args = None
    dynamic_result = None

    def __init__(self, method, args):
        self.dynamic_method_id = str(uuid.uuid4())
        self.dynamic_method_method = method
        self.dynamic_method_args = args

    def _get_item(self, item, is_iter=False):
        self.dynamic_result = super()._get_item(item, is_iter)
        return self.dynamic_result

    def executable_instance(self):
        executable_method = ExecutableMethod()
        executable_method.executable_method_id = self.dynamic_method_id
        executable_method.executable_method_method = self.dynamic_method_method
        executable_method.executable_method_args = []
        for arg in self.dynamic_method_args:
            if isinstance(arg, DynamicObject):
                executable_method.executable_method_args.append(arg.executable_instance())
            else:
                executable_method.executable_method_args.append(arg)
        return executable_method

    def get_result(self):
        if Context.results:
            for k, v in Context.results.items():
                if self.dynamic_method_id == k:
                    return v
        return None
