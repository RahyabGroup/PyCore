__author__ = 'H.Rouhani'

from os.path import dirname, split, splitext
from flask import Blueprint

this_directory = splitext(dirname(__file__))[0]
upward_directory = split(dirname(this_directory))[1]

version_path = ('/api/%s' % upward_directory.replace('_', '.'))
apis = Blueprint('token', __name__)

from pyclaim.domain.aggregates.token.app.v1_0.rest.api.internal import token_service
