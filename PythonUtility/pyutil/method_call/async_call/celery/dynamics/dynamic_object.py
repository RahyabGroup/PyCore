from pyutil.method_call.async_call.celery.dynamics.executable_adapter import ExecutableAdapter

__author__ = 'Hooman Familrouhani'


class DynamicObject(ExecutableAdapter):
    def __getattr__(self, item):
        return self._get_item(item)

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self._get_item(item, True)

    def _get_item(self, item, is_iter=False):
        from pyutil.method_call.async_call.celery.dynamics.dynamic_result import DynamicResult
        result_info = DynamicResult(item, self, is_iter)
        return result_info

    def executable_instance(self):
        raise NotImplementedError()

    def get_result(self):
        raise NotImplementedError()
