import asyncio
import functools

from pyfacil.web.rest.client.synchronous import requests as sync_requests

__author__ = 'H.Rouhani'


@asyncio.coroutine
def get(url, params=None, **kwargs):
    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, functools.partial(sync_requests.get, url, params, **kwargs))
    return (yield from fut)


@asyncio.coroutine
def post(url, data=None, json=None, **kwargs):
    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, functools.partial(sync_requests.post, url, data, json, **kwargs))
    return (yield from fut)


@asyncio.coroutine
def put(url, data=None, **kwargs):
    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, functools.partial(sync_requests.put, url, data, **kwargs))
    return (yield from fut)


@asyncio.coroutine
def patch(url, data=None, **kwargs):
    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, functools.partial(sync_requests.patch, url, data, **kwargs))
    return (yield from fut)


@asyncio.coroutine
def delete(url, **kwargs):
    loop = asyncio.get_event_loop()
    fut = loop.run_in_executor(None, functools.partial(sync_requests.delete, url, **kwargs))
    return (yield from fut)
