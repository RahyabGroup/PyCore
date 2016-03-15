import asyncio
import functools
import pymongo
from pydal.mongo.gridfs.gridfs_read import GridfsRead

__author__ = 'H.Rouhani'


class AsyncGridfsRead(GridfsRead):
    def get(self, id):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().get, id))
        return (yield from fut)

    def find_one(self, query):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().find_one, query))
        return (yield from fut)

    def find_many(self, query, skip=0, take=10, sort={'_id': pymongo.DESCENDING}):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().find_many, query, skip, take, sort))
        return (yield from fut)

    def is_available_id(self, id):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().is_available_id, id))
        return (yield from fut)

    def is_available(self, query):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().is_available, query))
        return (yield from fut)
