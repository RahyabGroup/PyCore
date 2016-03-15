from celery import Celery
import dill
import kombu
from kombu.five import BytesIO

__author__ = 'H.Rouhani'

celery_app = None


def initialize(app_module_name, backend, broker, **config):
    registry = kombu.serialization.registry
    kombu.serialization.pickle = dill

    registry.unregister('pickle')

    def pickle_loads(s, load=dill.load):
        return load(BytesIO(s))

    def pickle_dumps(obj, dumper=dill.dumps):
        return dumper(obj, protocol=kombu.serialization.pickle_protocol)

    registry.register('pickle', pickle_dumps, pickle_loads,
                      content_type='application/x-python-serialize',
                      content_encoding='binary')
    global celery_app
    celery_app = Celery(app_module_name, backend=backend, broker=broker)
    celery_app.conf.update(config)
    return celery_app
