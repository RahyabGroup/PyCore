import os
import re
from importlib.machinery import SourceFileLoader
import logging

from flask import Flask

from flask_cors import CORS

from pyfacil.web.rest.builder.app_builder import AppBuilder
from pyfacil.web.rest.flask.response import main_handler

__author__ = 'H.Rouhani'


class FlaskAppBuilder(AppBuilder):
    aggregate_modules = None
    api_variable_name = None
    version_path_variable_name = None
    variables_file_name = None
    app_directory_name = None
    rest_directory_name = None
    version_directory_name = None

    def __init__(self, aggregate_modules, log_path=None, log_level='DEBUG',
                 api_variable_name='apis', version_path_variable_name='version_path',
                 variables_file_name='__init__.py', app_directory_name='app',
                 rest_directory_name='rest', version_directory_name='v1_0'):
        self.aggregate_modules = aggregate_modules
        self.log_path = log_path
        self.log_level = log_level
        self.api_variable_name = api_variable_name
        self.version_path_variable_name = version_path_variable_name
        self.variables_file_name = variables_file_name
        self.app_directory_name = app_directory_name
        self.rest_directory_name = rest_directory_name
        self.version_directory_name = version_directory_name

    def _init_app(self):
        app = Flask(__name__)
        return app

    def _build_logger(self, app):
        if self.log_path:
            file_handler = logging.FileHandler(self.log_path)
            file_handler.setLevel(self.log_level)
            app.logger.addHandler(file_handler)
        elif self.log_level:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            app.logger.addHandler(console_handler)

    def _build_endpoints(self, app):
        for aggregate_module in self.aggregate_modules:
            for root, _, __ in os.walk(aggregate_module.__path__[0]):
                if root.endswith("{sep}{app}{sep}{ver}{sep}{rest}".format(sep=os.sep, app=self.app_directory_name, ver=self.version_directory_name, rest=self.rest_directory_name)):
                    r = re.search('(%s.*)' % aggregate_module.__package__, root.replace(os.sep, '.'))
                    module_name = r.group()
                    api_module = SourceFileLoader(module_name, '{}/{}'.format(root, self.variables_file_name)).load_module()
                    if hasattr(api_module, self.api_variable_name) and hasattr(api_module, self.version_path_variable_name):
                        app.register_blueprint(api_module.apis, url_prefix=api_module.version_path)
            app.register_blueprint(main_handler)

    def _build_cors(self, app):
        CORS(app)
