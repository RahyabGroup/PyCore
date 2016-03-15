import uuid

from pyutil.method_call.async_call.celery.executables.executable_scope import ExecutableScope

from pyutil.method_call.async_call.celery.dynamics.executable_adapter import ExecutableAdapter

__author__ = 'Hooman Familrouhani'


class DynamicScope(ExecutableAdapter):
    _id = None
    dynamic_methods = []
    hyper_mode = None

    def __init__(self):
        self._id = str(uuid.uuid4())
        self.hyper_mode = True

    def add_dynamic_method(self, dynamic_method):
        self.dynamic_methods.append(dynamic_method)

    def execute(self):
        self.hyper_mode = False
        executable_scope = self.executable_instance()
        return executable_scope.execute()

    def executable_instance(self):
        executable_scope = ExecutableScope()
        executable_scope.executable_methods = [dynamic_method.executable_instance() for dynamic_method in self.dynamic_methods]
        return executable_scope
