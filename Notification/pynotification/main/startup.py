import os
from pyfacil.web.rest.builder.flask.flask_app_builder import FlaskAppBuilder
from pynotification.domain import aggregates

__author__ = 'Hooman Familrouhani'

app_mode = os.environ.get('NOTIFICATION_CFG_MODE', None)

if app_mode == "dev.cfg" or not app_mode:
    app = FlaskAppBuilder([aggregates]).construct()
    app.run(host="localhost", port=8084, threaded=True)
