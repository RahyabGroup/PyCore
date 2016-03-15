import asyncio
import functools
from pydal.mongo.write import WriteCommand

__author__ = 'H.Rouhani'


class AsyncWriteCommand(WriteCommand):
    def save(self, data):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().save, data))
        yield from fut

    def add(self, data):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().add, data))
        yield from fut

    def edit(self, data):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().edit, data))
        yield from fut

    def edit_by_condition(self, first_query, second_query, multi=True):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().edit_by_condition, first_query, second_query, multi))
        yield from fut

    def remove_by_id(self, id_string):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().remove_by_id, id_string))
        yield from fut

    def remove_by_condition(self, query):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().remove_by_condition, query))
        yield from fut

    def remove_all(self):
        loop = asyncio.get_event_loop()
        fut = loop.run_in_executor(None, functools.partial(super().remove_all))
        yield from fut
