from pyutil.method_call.async_call.celery.dynamics.dynamic_scope import DynamicScope

__author__ = 'Hooman Familrouhani'


class Context:
    scope = None
    results = None
    do_execute = None

    def __enter__(self):
        if not Context.scope or not Context.scope.hyper_mode:
            self.do_execute = True
            Context.scope = DynamicScope()
        else:
            self.do_execute = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.do_execute:
            Context.results = Context.scope.execute()
