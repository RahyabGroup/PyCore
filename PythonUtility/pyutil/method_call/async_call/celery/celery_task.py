from functools import wraps

from pyutil.method_call.async_call.celery.context import Context

from pyutil.method_call.async_call.celery.dynamics.dynamic_method import DynamicMethod

__author__ = 'Hooman Familrouhani'


def celery_task(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if Context.scope.hyper_mode:
            dynamic_method = DynamicMethod(f, args)
            Context.scope.add_dynamic_method(dynamic_method)
            return dynamic_method
        else:
            return f(*args, **kwargs)
    return decorated_function
