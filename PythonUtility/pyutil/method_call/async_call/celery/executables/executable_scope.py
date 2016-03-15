from celery import chain
from celery.contrib.methods import task_method
from pyutil.method_call.async_call.celery.application import celery_app

__author__ = 'Hooman Familrouhani'


class ExecutableScope:
    executable_methods = []

    def execute(self):
        return self.do_execute.delay().get().get()

    @celery_app.task(filter=task_method)
    def do_execute(self):
        res = chain(*self.__signatures())()
        return res

    def __signatures(self):
        signatures = []
        for method_info in self.executable_methods:
            signatures.append(method_info.signature())
        return signatures
