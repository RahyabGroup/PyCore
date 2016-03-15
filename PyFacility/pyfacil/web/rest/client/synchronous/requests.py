import requests
from pyfacil.web.rest.client.http_response_service import http_response_make

__author__ = 'H.Rouhani'


def get(url, params=None, **kwargs):
    return http_response_make(requests.get(url, params, **kwargs))


def post(url, data=None, json=None, **kwargs):
    return http_response_make(requests.post(url, data, json, **kwargs))


def put(url, data=None, **kwargs):
    return http_response_make(requests.put(url, data, **kwargs))


def patch(url, data=None, **kwargs):
    return http_response_make(requests.patch(url, data, **kwargs))


def delete(url, **kwargs):
    return http_response_make(requests.delete(url, **kwargs))
