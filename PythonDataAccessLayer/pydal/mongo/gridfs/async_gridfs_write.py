import asyncio
import functools

from pydal.mongo.gridfs.gridfs_write import GridfsWrite

__author__ = 'H.Rouhani'


class AsyncGridfsWrite(GridfsWrite):
    def add(self, binary_data, **kwargs):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().add, binary_data, **kwargs))
        yield from fut

    def remove(self, id):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().remove, id))
        yield from fut

    def remove_by_condition(self, query):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().remove_by_condition, query))
        yield from fut
