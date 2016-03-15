import asyncio
import functools

import pymongo

from pydal.mongo.read import ReadCommand

__author__ = 'H.Rouhani'


class AsyncReadCommand(ReadCommand):
    def count(self, query=None):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().count, query))
        return (yield from fut)

    def find_one(self, query, fields=[]):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().find_one, query, fields))
        return (yield from fut)

    def find_many(self, query, fields=[], skip=0, take=50, sort={'_id': pymongo.DESCENDING}):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().find_many, query, fields, skip, take, sort))
        return (yield from fut)

    def is_available(self, query):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().is_available, query))
        return (yield from fut)

    def aggregate(self, fields=[], skip=0, take=50, sort={'_id': pymongo.DESCENDING}, query=[]):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().aggregate, fields, skip, take, sort, query))
        return (yield from fut)

    def aggregate_count(self, query=[], fields=[]):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().aggregate_count, query, fields))
        return (yield from fut)
