from collections import OrderedDict

from celery.contrib.methods import task_method

from pyutil.method_call.async_call.celery.application import celery_app
from pyutil.method_call.async_call.celery.executables.executable_object import ExecutableObject

__author__ = 'Hooman Familrouhani'


class ExecutableMethod(ExecutableObject):
    executable_method_id = None
    executable_method_method = None
    executable_method_args = None

    def signature(self):
        return self.run.s(self)

    @celery_app.task(filter=task_method)
    def run(first, second):
        self = first if second is None or second is first else second
        previous_results = OrderedDict() if second is None or second is first else first
        required_params = self.get_normalized_args(previous_results)
        result = self.executable_method_method(*required_params)
        previous_results[self.executable_method_id] = result
        return previous_results

    def get_normalized_args(self, previous_results):
        result = []
        for arg in self.executable_method_args:
            if isinstance(arg, ExecutableObject):
                result.append(arg.get_arg_value(previous_results))
            else:
                result.append(arg)
        return result

    def get_arg_value(self, previous_results):
        return previous_results[self.executable_method_id]
