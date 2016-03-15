import asyncio
from functools import wraps
from concurrent.futures import ThreadPoolExecutor

__author__ = 'H.Rouhani'


class AsyncInvoker:
    def async_invoke(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                loop = self._get_event_loop()
                try:
                    loop.set_default_executor(ThreadPoolExecutor(20))
                    task = loop.create_task(self._call_as_coroutine(f, *args, **kwargs))
                    loop.run_until_complete(asyncio.gather(*asyncio.Task.all_tasks(loop)))
                    return task.result()
                except Exception as ex:
                    loop.close()
                    raise ex

            return decorated_function

        return decorator

    @asyncio.coroutine
    def _call_as_coroutine(self, f, *args, **kwargs):
        return (yield from f(*args, **kwargs))

    def _get_event_loop(self):
        loop = asyncio.get_event_loop()
        if not loop or loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        return loop
